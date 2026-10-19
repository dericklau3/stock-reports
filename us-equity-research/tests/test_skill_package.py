"""美股研究 Skill 的结构与格式回归测试。

运行：uv run --with pyyaml python -B -m unittest discover -s us-equity-research/tests -v
本文件只验证规则、路径和模板结构，不代替实际金融研究质量检查。
"""
import re
import shutil
import subprocess
import sys
import tempfile
import json
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def local_links(path):
    """解析 Markdown 内相对链接（忽略外部 URL 和锚点）。"""
    return [
        item.split("#", 1)[0] for item in
        re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8"))
        if not item.startswith(("http:", "https:", "#", "mailto:"))
    ]


class SkillPackageTests(unittest.TestCase):
    def test_discovery_metadata(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        metadata = yaml.safe_load(content.split("---", 2)[1])
        self.assertEqual(metadata["name"], ROOT.name)
        self.assertIsInstance(metadata["description"], str)
        self.assertTrue(metadata["description"].strip())
        self.assertLessEqual(len(metadata["description"]), 1024)
        self.assertIn("# 美股个股研究", content)

    def test_single_discoverable_skill(self):
        self.assertEqual(sorted(ROOT.rglob("SKILL.md")), [ROOT / "SKILL.md"])

    def test_agent_config(self):
        config = yaml.safe_load((ROOT / "agents/openai.yaml").read_text(encoding="utf-8"))
        interface = config["interface"]
        for field in ("display_name", "short_description", "default_prompt"):
            self.assertTrue(isinstance(interface.get(field), str) and interface[field].strip())
        self.assertTrue(25 <= len(interface["short_description"]) <= 64)
        self.assertIn("$" + ROOT.name, interface["default_prompt"])
        self.assertIn("中文", interface["default_prompt"])

    def test_reference_links(self):
        docs = [ROOT / "SKILL.md", *sorted((ROOT / "references").glob("*.md"))]
        for file in docs:
            for link in local_links(file):
                target = (file.parent / link).resolve()
                with self.subTest(file=file.name, link=link):
                    self.assertFalse(Path(link).is_absolute())
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.is_file())

    def test_all_references_reachable(self):
        seen, pending = set(), [ROOT / "SKILL.md"]
        while pending:
            current = pending.pop().resolve()
            if current in seen:
                continue
            seen.add(current)
            for link in local_links(current):
                target = (current.parent / link).resolve()
                if target.is_file() and target.suffix == ".md":
                    pending.append(target)
        for ref in (ROOT / "references").glob("*.md"):
            self.assertIn(ref.resolve(), seen, ref.name)

    def test_package_isolated_from_sibling_skills(self):
        # A sibling Chinese package must not invalidate this portable skill.
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / ROOT.name
            shutil.copytree(ROOT, target)
            sibling = Path(tmp) / "cn" / "another-skill"
            sibling.mkdir(parents=True)
            (sibling / "SKILL.md").write_text("unrelated skill", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(target / "tests/test_skill_package.py"),
                 "SkillPackageTests.test_reference_links",
                 "SkillPackageTests.test_all_references_reachable"],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_report_structure(self):
        # Protect the agreed nine-section layout, not wording or example years.
        template = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        sections = re.findall(r"^### (\d+)\. (.+)$", template, re.M)
        self.assertEqual([int(n) for n, _ in sections], list(range(1, 10)))
        bodies = re.split(r"^### \d+\. .+$", template, flags=re.M)[1:]
        for number, width in {2: 3, 3: 3, 6: 2, 7: 2, 8: 3, 9: 3}.items():
            rows = [line for line in bodies[number - 1].splitlines() if line.startswith("|")]
            self.assertGreaterEqual(len(rows), 3)
            self.assertTrue(all(len(row.strip("|").split("|")) == width for row in rows))
        financial_rows = [line for line in bodies[3].splitlines() if line.startswith("|")]
        widths = {len(row.strip("|").split("|")) for row in financial_rows}
        self.assertEqual(len(widths), 1)
        self.assertGreaterEqual(widths.pop(), 4)

    def test_prepare_blind_behavior_packet(self):
        script = ROOT / "tests/prepare_behavior_eval.py"
        self.assertTrue(script.is_file(), "Missing repeatable blind evaluation packet builder")
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "packet"
            result = subprocess.run([sys.executable, "-B", str(script), str(dest)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            manifest = json.loads((dest / "manifest.json").read_text())
            inputs = (dest / "inputs.md").read_text()
            source = (ROOT / "tests/behavioral-cases.md").read_text().split("## 验收标准")[0]
            self.assertEqual(inputs, source)
            self.assertEqual(manifest["case_ids"], list(range(1, 22)))
            self.assertFalse((dest / "skill/tests").exists())
            self.assertEqual((dest / "skill/SKILL.md").read_bytes(), (ROOT / "SKILL.md").read_bytes())
            import hashlib
            for name, digest in manifest["sha256"].items():
                self.assertEqual(hashlib.sha256((dest / name).read_bytes()).hexdigest(), digest)
            marker = dest / "responses.md"
            marker.write_text("preserve existing evaluation")
            retry = subprocess.run([sys.executable, "-B", str(script), str(dest)],
                                   capture_output=True, text=True)
            self.assertNotEqual(retry.returncode, 0)
            self.assertEqual(marker.read_text(), "preserve existing evaluation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
