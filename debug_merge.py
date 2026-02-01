import result
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('custom_aliases.json', 'r', encoding='utf-8') as f:
    aliases = json.load(f)

for k, v in aliases.items():
    if '네스티' in k:
        nk = result.normalize_product(k)
        nv = result.normalize_product(v)
        print(f"Original: {k}")
        print(f"  -> Target: {v}")
        print(f"  -> Keys Match: {nk['match_key'] == nv['match_key']}")
        print(f"  -> Key K: {nk['match_key']}")
        print(f"  -> Key V: {nv['match_key']}")
        print("-" * 30)
