import result
import json

names = [
    '네스티 더블 슬로우 블로우 하이민트 30ml',
    '네스티 슬로우 블로우 하이민트 30ml'
]

for n in names:
    norm = result.normalize_product(n)
    print(norm['match_key'])
