"""Create a frozen, answer-free evaluation packet using only the standard library."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


def prepare(destination):
    root = Path(__file__).resolve().parents[1]
    cases = (root / 'tests/behavioral-cases.md').read_text(encoding='utf-8')
    inputs, separator, _ = cases.partition('## 验收标准')
    if not separator:
        raise ValueError('Missing answer boundary; refusing to expose the full case file')
    ids = [int(n) for n in re.findall(r'^(\d+)\. \*\*', inputs, re.M)]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError('Missing or duplicate case IDs')
    destination.mkdir(parents=True, exist_ok=False)
    skill = destination / 'skill'
    skill.mkdir()
    shutil.copy2(root / 'SKILL.md', skill / 'SKILL.md')
    shutil.copytree(root / 'references', skill / 'references')
    (destination / 'inputs.md').write_text(inputs, encoding='utf-8')
    files = [destination / 'inputs.md', skill / 'SKILL.md', *sorted((skill / 'references').glob('*.md'))]
    manifest = {
        'case_ids': ids,
        'sha256': {str(p.relative_to(destination)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
    }
    (destination / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(destination.resolve())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='A new directory; existing results are never overwritten')
    prepare(parser.parse_args().destination)
