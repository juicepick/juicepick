import result

def check_missing():
    print("데이터를 불러오는 중입니다...")
    data, _ = result.process_data()
    
    missing_all = []
    missing_verified = []
    
    for key, item in data.items():
        if not item.get('image'):
            missing_all.append(item)
            # 2곳 이상에서 판매중인 상품만 '검증된 상품'으로 간주
            if len(item['prices']) >= 2:
                missing_verified.append(item)
                
    print(f"\n📊 이미지 누락 현황 분석")
    print(f"전체 상품 중 이미지 없음: {len(missing_all)}개")
    print(f"검증된 상품(2곳 이상 판매) 중 이미지 없음: {len(missing_verified)}개")
    
    if len(missing_verified) > 0:
        print("\n[예시 상품들]")
        for item in missing_verified[:5]:
            print(f"- {item['display_name']} ({len(item['prices'])}곳 판매)")

if __name__ == "__main__":
    check_missing()
