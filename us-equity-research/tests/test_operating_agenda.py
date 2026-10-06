"""Offline structural checks for the portable operating-agenda research rules."""
import re
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parent
MAIN = (SKILL_ROOT / 'SKILL.md').read_text(encoding='utf-8')
REF = (SKILL_ROOT / 'references/operating-agenda-execution-progress.md').read_text(encoding='utf-8')
CN = (REPO_ROOT / 'cn/us-equity-research/SKILL_CN.md').read_text(encoding='utf-8')
README = (REPO_ROOT / 'cn/us-equity-research/README.md').read_text(encoding='utf-8')
AGENT = (SKILL_ROOT / 'agents/openai.yaml').read_text(encoding='utf-8')


def section(text, title):
    marker = '## ' + title + '\n'
    start = text.index(marker)
    end = text.find('\n## ', start + len(marker))
    return text[start:] if end < 0 else text[start:end]


class OperatingAgendaTests(unittest.TestCase):
    def test_frontmatter_and_portability(self):
        self.assertTrue(MAIN.startswith('---\n'))
        fm = MAIN.split('---', 2)[1]
        self.assertRegex(fm, r'(?m)^name: us-equity-research$')
        description_match = re.search(r'(?m)^description: (.+)$', fm)
        assert description_match is not None, 'Missing description in frontmatter'
        description = description_match.group(1)
        self.assertLessEqual(len(description), 60)
        self.assertTrue(description.endswith('.'))
        for text in [MAIN, REF, AGENT]:
            self.assertNotIn('/home/ubuntu/', text)

    def test_main_reference_resolves(self):
        links = set(re.findall(r'references/[\w./-]+\.md', MAIN))
        self.assertIn('references/operating-agenda-execution-progress.md', links)
        for link in links:
            self.assertTrue((SKILL_ROOT / link).is_file(), link)

    def test_chinese_reference_links_resolve(self):
        for text, path in [(CN, REPO_ROOT / 'cn/us-equity-research/SKILL_CN.md'),
                           (README, REPO_ROOT / 'cn/us-equity-research/README.md')]:
            links = re.findall(r'\]\(([^)]+)\)', text)
            self.assertTrue(any('operating-agenda-execution-progress.md' in x for x in links))
            for link in links:
                if not link.startswith(('http:', 'https:', '#')):
                    self.assertTrue((path.parent / link.split('#')[0]).resolve().is_file(), link)

    def test_workflow_and_both_templates_require_progress(self):
        self.assertIn('Operating Agenda and Execution Progress (Required)', MAIN)
        for title in ['Core Research Workflow', 'Deep Company Research Template', 'Post-Earnings Tracking Template']:
            self.assertIn('Execution Progress', section(MAIN, title))
        for title in ['核心研究流程', '深度个股研究模板', '财报后追踪模板']:
            block = section(CN, title)
            self.assertTrue('进度' in block or '当前阶段' in block)

    def test_tracker_preserves_commitments_and_stage_deltas(self):
        self.assertIn('Preserve original commitments', MAIN)
        self.assertIn('prior stage → new evidence → current stage', MAIN)
        self.assertIn('上次阶段 → 新证据 → 当前阶段', CN)
        self.assertIn('原始承诺', CN)
        self.assertIn('no new public evidence', REF)

    def test_four_dimensions_and_evidence_are_separate(self):
        for value in ['Technical/product', 'Regulatory/legal', 'Commercial/adoption', 'Economics/shareholder', 'Company-reported', 'Corroborated', 'Independently observed']:
            self.assertIn(value, REF)
        self.assertIn('do not invent percentage completion', REF)
        self.assertIn('不编完成百分比', CN)
        self.assertIn('not independent corroboration', REF)

    def test_pre_revenue_progress_is_acknowledged_without_overclaim(self):
        self.assertIn('unknown does not mean zero', REF)
        self.assertIn('does not erase verified engineering or adoption progress', REF)
        self.assertIn('尚未盈利', CN)
        self.assertIn('未知不是零，也不是成功', CN)
        self.assertIn('not common-equity income', REF)

    def test_sector_gates_and_core_business_initiatives(self):
        for value in ['Software/AI/cloud', 'Semiconductors/hardware', 'Industrial/energy/infrastructure', 'Space/defense', 'Biopharma', 'Consumer/franchise', 'Fintech/payments/crypto', 'Insurance/turnarounds', 'M&A']:
            self.assertIn(value, REF)
        self.assertIn('existing profit engine', REF)
        self.assertIn('not just high-profile new projects', REF)
        self.assertIn('不是', CN)

    def test_outputs_and_agent_prompt_include_next_gate(self):
        for text in [MAIN, CN, README]:
            self.assertIn('下一关', text)
        self.assertIn('next gate and bottleneck', AGENT)
        self.assertIn('per-share returns', AGENT)
        self.assertIn('before valuation', AGENT)
        self.assertIn('正在做什么 / 最新进度 / 下一关', section(MAIN, 'Output Style'))

    def test_existing_research_and_valuation_modes_remain(self):
        self.assertIn('Use only these two modes', section(MAIN, 'Mode Selection'))
        self.assertIn('只支持两种模式', section(CN, '模式选择'))
        self.assertIn('not a third mode', MAIN)
        for heading in ['Guardrails', 'Valuation Discipline', 'Risk / Reward Framework', 'Four Investor-Style Decision Lenses']:
            self.assertTrue(section(MAIN, heading))
        self.assertIn('1-year high forward P/E', MAIN)
        self.assertIn('1-year low forward P/E', MAIN)


if __name__ == '__main__':
    unittest.main(verbosity=2)
