import result
import json

names = [
    "네스티 더블 블로우 슬로우 30ml",
    "네스티 더블 슬로우 블로우 30ml",
    "네스티 블로우 슬로우 30ml",
    "네스티 슬로우 블로우 30ml",
    "네스티 더블 슬로우 블로우 하이민트 30ml",
    "네스티 슬로우 블로우 하이민트 30ml"
]

results = []
for n in names:
    norm = result.normalize_product(n)
    results.append({
        "name": n,
        "key": norm['match_key'],
        "display": norm['display_name']
    })

with open('key_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
