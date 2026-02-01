import firebase_admin
from firebase_admin import credentials, db
import os
import sys

def test_connection():
    if not os.path.exists("key.json"):
        print("❌ key.json 파일이 없습니다!")
        return

    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate("key.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://juicehunter-default-rtdb.asia-southeast1.firebasedatabase.app'
            })
        print("✅ Firebase SDK 초기화 성공!")
        
        # Test DB connection
        ref = db.reference('test_connection')
        ref.set("Hello Firebase")
        print("✅ 데이터베이스 쓰기 테스트 성공!")
        print("🎉 Firebase가 정상적으로 연결되었습니다.")
        
    except Exception as e:
        print(f"❌ 연결 실패: {e}")

if __name__ == "__main__":
    test_connection()
