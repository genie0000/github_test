# 파일 경로: ~/study/linux/1_hello.py

import os # 운영체제와 관련된 작업(폴더 만들기, 파일경로 다루기 등)을 도와주는 도구이다.

def main():
    try:
        os.makedirs('/test', exist_ok = True)  # /test 디렉토리 생성 (이미 있으면 무시)
        with open('/test/hello.txt', 'w') as f: # w(쓰기모드)로 파일을 연다.
            f.write('Hello Linux') # 파일 안에 Hello Linux를 작성한다.
        print("파일 생성 완료!")

    except PermissionError: # 만약 권한이 없어서 에러가 나면 아래 print문 출력
        print("Permission denied: 관리자 권한이 필요합니다.")

    except Exception as e: # 다른 에러가 발생하면, 그 에러 내용을 출력
        print(f"오류 발생: {e}")

# 직접 실행할 때만 특정 함수를 실행하게 해준다.
if __name__ == "__main__":
    main()