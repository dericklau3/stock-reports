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

    def test_short_progress_summary_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        progress = (ROOT / 'references/operating-agenda-execution-progress.md').read_text(encoding='utf-8')
        self.assertIn('one three-column table with normally 3–5 rows', progress)
        self.assertIn('| 重点项目 | 为什么做？希望达到什么结果？ | 当前进展与下一步 |', progress)
        self.assertIn('The purpose column must answer', progress)
        self.assertIn('every initiative must explain its purpose', template)
        self.assertIn('No 3.1/3.2/3.3 item-by-item essays', progress)
        self.assertIn('Never generate the former five-column initiative inventory', template)
        self.assertIn('only the top 3–5 milestones', skill)

    def test_beginner_financial_summary_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        financial = template.split('3. **Financial Position / 财务状况：收入、利润和现金**', 1)[1].split('4. **Management and Capital Allocation**', 1)[0]
        self.assertIn('one multi-period financial table', skill)
        self.assertIn('5–8 important rows', skill)
        self.assertIn('| 指标 | FY2024 | FY2025 | H1 2026 | TTM至2026Q2 |', financial)
        self.assertIn('| GAAP收入 |', financial)
        self.assertIn('| GAAP毛利 |', financial)
        self.assertIn('| 自由现金流 |', financial)
        self.assertIn('<small class="financial-glossary">', financial)
        self.assertIn('one paragraph starting 总结：', financial)
        self.assertIn('Avoid false comparisons between full fiscal years and H1', financial)
        self.assertIn('period-comparison table → small-font definitions → one summary paragraph', template)
        self.assertNotIn('3. **Financial Deep Dive**', template)

    def test_compact_reader_facing_valuation_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        valuation = (ROOT / 'references/valuation.md').read_text(encoding='utf-8')
        section = template.split('5. **Valuation / 估值分析：当前股价贵不贵？**', 1)[1].split('6. **Catalysts and Monitoring Plan**', 1)[0]
        self.assertIn('| 关键指标 | 估算结果 |', section)
        for key in ('保守情景估值', '基础情景估值', '乐观情景估值'):
            self.assertIn(key, section)
        self.assertIn('one concise summary paragraph starting 总结：', section)
        self.assertIn('discounted estimates of today', section)
        self.assertNotIn('5. **Valuation Work**', template)
        self.assertIn('## Beginner-readable valuation display', skill)
        self.assertIn('## What the reader sees versus what the research retains', valuation)

    def test_compact_catalysts_and_monitoring_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        section = template.split('6. **Future Events to Watch / 未来值得关注的事件**', 1)[1].split('7. **Key Investment Risks / 主要投资风险**', 1)[0]
        self.assertIn('## Concise future events and monitoring', skill)
        self.assertIn('| 重要事件 | 为什么值得关注 |', section)
        self.assertIn('3–5 key upcoming events', section)
        self.assertIn('one 2–3-sentence paragraph beginning 总结：', section)
        self.assertIn('include it only if officially confirmed', section)
        self.assertIn('do not mechanically repeat the earlier', section)
        self.assertNotIn('6. **Catalysts and Monitoring Plan**', template)
        self.assertIn('same **重要事件 | 为什么值得关注** two-column format', template)

    def test_compact_investment_risks_contract(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        template = (ROOT / 'references/report-templates.md').read_text(encoding='utf-8')
        section = template.split('7. **Key Investment Risks / 主要投资风险**', 1)[1].split('8. **Four Investor-Style Decision Lenses**', 1)[0]
        self.assertIn('## Beginner-readable investment risks', skill)
        self.assertIn('| 主要风险 | 可能产生什么影响 | 需要警惕的信号 |', section)
        self.assertIn('normally 4–5 company-specific material risks', section)
        self.assertIn('one 2–3-sentence paragraph starting 总结：', section)
        self.assertIn('No reader-facing "判断/严重度"', section)
        self.assertIn('observable warning signals', section)
        self.assertIn('not in extra public tables', section)
        self.assertNotIn('7. **Risk Register**', template)

    def test_chinese_maintenance_links(self):
        directory = ROOT.parent / 'cn' / ROOT.name
        if not directory.is_dir():
            self.skipTest('Standalone package has no repository maintenance mirror')
        for path in directory.glob('*.md'):
            for link in local_links(path):
                self.assertTrue((path.parent / link).resolve().is_file(), (path, link))


if __name__ == '__main__':
    unittest.main(verbosity=2)
