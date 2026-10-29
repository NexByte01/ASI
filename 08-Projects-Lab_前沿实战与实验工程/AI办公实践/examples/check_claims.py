"""Check citation IDs and literal evidence only; human labels are supplied data."""
import json
from pathlib import Path
import sys


def check_claim(claim, documents):
    text = documents.get(claim['source_id'])
    return {'claim': claim['claim'], 'source_id': claim['source_id'],
            'citation_exists': text is not None,
            'quote_in_source': text is not None and bool(claim['quote']) and claim['quote'] in text,
            'semantic_support': 'not_automatically_evaluated',
            'human_reference': claim['human_reference']}


def main():
    base = Path(__file__).parent
    documents = {d['id']:d['text'] for d in json.loads((base/'office_materials.json').read_text(encoding='utf-8'))['documents']}
    claims = json.loads((base/'claims.json').read_text(encoding='utf-8'))
    print(json.dumps([check_claim(c, documents) for c in claims], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
