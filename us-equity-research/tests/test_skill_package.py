"""Package contract checks, not proof of research quality. Requires PyYAML.

Run: python -B -m unittest discover -s us-equity-research/tests -v
Works in a standalone installed skill; Chinese maintenance docs are optional.
Behavioral evaluation instructions live in behavioral-cases.md.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def local_links(path):
    return [link.split('#')[0] for link in
            re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8'))
            if not link.startswith(('https:', 'http:', '#', 'mailto:'))]


class SkillPackageTests(unittest.TestCase):
    def test_discovery_metadata(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\n'))
        metadata = yaml.safe_load(text.split('---', 2)[1])
        self.assertEqual(metadata['name'], ROOT.name)
        self.assertIsInstance(metadata['description'], str)
        self.assertTrue(metadata['description'].strip())
        self.assertLessEqual(len(metadata['description']), 1024)

    def test_ui_metadata_contract(self):
        config = yaml.safe_load((ROOT / 'agents/openai.yaml').read_text())
        interface = config.get('interface', {})
        for key in ('display_name', 'short_description', 'default_prompt'):
            self.assertIsInstance(interface.get(key), str, key)
            self.assertTrue(interface[key].strip())
        self.assertIn('$' + ROOT.name, interface['default_prompt'])
        self.assertTrue(25 <= len(interface['short_description']) <= 64)

    def test_runtime_links_are_portable(self):
        files = [ROOT / 'SKILL.md', *sorted((ROOT / 'references').glob('*.md'))]
        for path in files:
            for link in local_links(path):
                target = (path.parent / link).resolve()
                with self.subTest(path=path.name, link=link):
                    self.assertFalse(Path(link).is_absolute())
                    self.assertTrue(target.is_relative_to(ROOT.resolve()))
                    self.assertTrue(target.is_file())

    def test_references_are_reachable_from_entrypoint(self):
        seen, pending = set(), [ROOT / 'SKILL.md']
        while pending:
            path = pending.pop().resolve()
            if path in seen:
                continue
            seen.add(path)
            for link in local_links(path):
                target = (path.parent / link).resolve()
                if target.is_file() and target.suffix == '.md':
                    pending.append(target)
        for path in (ROOT / 'references').glob('*.md'):
            self.assertIn(path.resolve(), seen, path.name)

    def test_single_three_item_report_summary(self):
        """Block regressions that bring back duplicate executive summaries."""
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        self.assertIn('Strictly prohibit any additional executive-overview section', skill)
        self.assertEqual(template.count('Open with **exactly three brief, reader-facing items**'), 2)
        self.assertEqual(template.count('Do **not** create a separate or numbered executive overview'), 2)
        # A reference to a forbidden title in a prohibition is OK; a section is not.
        forbidden_heading = re.compile(
            r'(?mi)^\\s*(?:\\d+\\.\\s*|\\#{1,6}\\s*)?'
            r'\\*{0,2}(?:Executive View|Executive Summary|执行摘要|先给结论)\\*{0,2}\\s*(?:[:：]|$)'
        )
        self.assertIsNone(forbidden_heading.search(template))
        self.assertNotIn('- **Confidence**:', template)
        self.assertNotIn('- **Time horizon**:', template)

    def test_beginner_business_model_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        self.assertIn('## Beginner-first business model', skill)
        for prompt in (
            'What does this company actually do?',
            'What customer problem does it solve?',
            'Who buys it and why?',
            'What is sold and how is the company paid?',
            'Where does the money go?',
        ):
            self.assertIn(prompt, template)
        self.assertIn('hypothetical illustration', template)
        self.assertIn('do not mistake partnerships', template.lower())

    def test_chinese_maintenance_links(self):
        directory = ROOT.parent / 'cn' / ROOT.name
        if not directory.is_dir():
            self.skipTest('Standalone package has no repository maintenance mirror')
        for path in directory.glob('*.md'):
            for link in local_links(path):
                self.assertTrue((path.parent / link).resolve().is_file(), (path, link))


if __name__ == '__main__':
    unittest.main(verbosity=2)
