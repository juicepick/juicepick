import result
names = [
    "네스티 더블 블로우 슬로우 30ml",
    "네스티 더블 슬로우 블로우 30ml",
    "네스티 블로우 슬로우 30ml",
    "네스티 슬로우 블로우 30ml",
    "네스티 더블 슬로우 블로우 하이민트 30ml",
    "네스티 슬로우 블로우 하이민트 30ml"
]
for n in names:
    norm = result.normalize_product(n)
    print(f"Name: {n}")
    print(f"  -> Key:  {norm['match_key']}")
    print(f"  -> Display: {norm['display_name']}")
    print("-" * 30)
