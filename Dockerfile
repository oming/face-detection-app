# 베이스 이미지 설정
FROM aaftio/face_recognition

# 작업 디렉토리 설정
WORKDIR /app

# 소스 코드 복사
COPY src/ /app/src/

# 실행 명령어
CMD ["python", "src/main.py"]
