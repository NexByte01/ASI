"""Decision-only offline permission demo; performs no tool/file operations."""
from pathlib import Path
import json


def decide(action, target, allowed_root):
    target, allowed_root = Path(target).resolve(), Path(allowed_root).resolve()
    if not target.is_relative_to(allowed_root):
        return 'deny'
    if action == 'read':
        return 'allow'
    if action == 'write_draft':
        return 'confirm'
    return 'deny'


if __name__ == '__main__':
    base = Path(__file__).parent
    cases = [('read', base/'office_materials.json'), ('write_draft', base/'draft.txt'),
             ('read', base.parent/'outside.txt'), ('delete', base/'office_materials.json')]
    print(json.dumps([{'action':a, 'decision':decide(a,p,base)} for a,p in cases], indent=2))
