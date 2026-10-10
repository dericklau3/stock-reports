"""美股研究 Skill 的结构与格式回归测试。

运行：python -B -m unittest discover -s us-equity-research/tests -v
本文件只验证规则、路径和模板结构，不代替实际金融研究质量检查。
"""
import re
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

    def test_no_chinese_mirror_folder(self):
        self.assertFalse((ROOT.parent / "cn").exists())
        for file in [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md")]:
            self.assertNotIn("../../cn/", file.read_text(encoding="utf-8"))

    def test_only_three_opening_items(self):
        content = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        template = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        for key in ("投资观点", "核心逻辑", "主要风险"):
            self.assertIn(key, template)
        self.assertIn("禁止", template)
        self.assertNotRegex(template, r"(?m)^#{1,5}\s+(?:Executive View|Executive Summary)")
        self.assertIn("开头仅保留三项", template)
        self.assertIn("不单独显示 Research view", content)

    def test_business_model(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        for label in ("公司具体卖什么", "解决什么问题", "谁会购买", "具体怎么收费", "哪些成本", "举例假设"):
            self.assertIn(label, content)

    def test_project_progress(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        progress = (ROOT / "references/operating-agenda-execution-progress.md").read_text(encoding="utf-8")
        header = "| 重点项目 | 为什么做？希望达到什么结果？ | 当前进展与下一步 |"
        self.assertIn(header, content)
        self.assertIn(header, progress)
        self.assertIn("3–5", content)
        self.assertIn("不再生成五列", progress)

    def test_historical_financial_table_glossary_summary(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        financial = content.split("### 3. 财务状况：收入、利润和现金", 1)[1].split("### 4. 管理层与资本分配", 1)[0]
        self.assertIn("| 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2 |", financial)
        for key in ("GAAP收入", "GAAP毛利", "GAAP经营损益", "经营现金流", "自由现金流"):
            self.assertIn(key, financial)
        self.assertIn('<small class="financial-glossary">', financial)
        self.assertIn("总结：", financial)
        self.assertIn("不能直接比较两者来计算同比", financial)

    def test_compact_valuation(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        section = content.split("### 5. 估值分析：当前股价贵不贵？", 1)[1].split("### 6. 未来值得关注的事件", 1)[0]
        self.assertIn("| 关键指标 | 估算结果 |", section)
        for key in ("保守情景估值", "基础情景估值", "乐观情景估值"):
            self.assertIn(key, section)
        self.assertIn("折现到今天的价值", section)
        self.assertIn("总结：", section)

    def test_future_events(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        section = content.split("### 6. 未来值得关注的事件", 1)[1].split("### 7. 主要投资风险", 1)[0]
        self.assertIn("| 重要事件 | 为什么值得关注 |", section)
        self.assertIn("3–5", section)
        self.assertIn("官方核实", section)
        self.assertIn("总结：", section)

    def test_investment_risks(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        section = content.split("### 7. 主要投资风险", 1)[1].split("### 8. 四种投资视角", 1)[0]
        self.assertIn("| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |", section)
        self.assertIn("4–5", section)
        self.assertIn("总结：", section)
        self.assertIn("不能", section)

    def test_four_lenses_and_no_final_repeat(self):
        content = (ROOT / "references/report-templates.md").read_text(encoding="utf-8")
        section = content.split("### 8. 四种投资视角", 1)[1].split("## 财报与重大事件跟踪模板", 1)[0]
        self.assertIn("| 投资视角 | 最关注什么 | 对公司的判断 |", section)
        for name in ("巴菲特式", "芒格式", "段永平式", "李录式"):
            self.assertIn("| " + name + " |", section)
        self.assertIn("完整深度报告的最后一段", section)
        self.assertNotRegex(content, r"(?m)^\s*(?:\d+\.\s*)?(?:Final Research Framework|最终研究结论)\s*$")
        self.assertIn("研究资料", (ROOT / "references/investor-lenses.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
