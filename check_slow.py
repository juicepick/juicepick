import re
with open('inventory_report.html', 'r', encoding='utf-8') as f:
    content = f.read()
titles = re.findall(r'<h3 class="product-title">(.*?)</h3>', content)
slow_total = [t.strip() for t in titles if '슬로우' in t]
print(f"Total entries for '슬로우': {len(slow_total)}")
for t in slow_total:
    print(f"- {t}")
