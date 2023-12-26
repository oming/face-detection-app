# face-detection-app

이미지에 얼굴 포함 여부에 따라 이미지를 구분합니다. 이 코드는 [face_recognition](https://github.com/ageitgey/face_recognition)을 사용합니다.

### 사용법

간단히 사용하기 위해 docker를 사용합니다.

```shell
docker build -t face-detection-app .
```

```shell
docker run --rm -v $(pwd)/input_images:/app/input_images face-detection-app
```

### 개발 테스트 방법

다음 명령어로 `src/main.py` 소스를 수정하여 테스트할 수 있습니다.

```shell
docker run -i -t --rm -v $(pwd):/app face-detection-app
```
