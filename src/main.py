import os
import face_recognition


def detect_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    print("face_locations = " + str(face_locations))

    return len(face_locations) > 0


def process_images(input_dir):
    # 입력 디렉토리 하위에 출력 디렉토리 생성
    output_dir_with_face = os.path.join(input_dir, "with_face")
    output_dir_without_face = os.path.join(input_dir, "without_face")

    print("output_dir_with_face = " + output_dir_with_face)
    print("output_dir_without_face = " + output_dir_without_face)

    # 출력 디렉토리 생성
    os.makedirs(output_dir_with_face, exist_ok=True)
    os.makedirs(output_dir_without_face, exist_ok=True)

    # 입력 디렉토리의 이미지 파일 목록 가져오기
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    print("total image_files =", len(image_files))

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        print("image_path = " + image_path)

        # 얼굴 검출
        has_face = detect_faces(image_path)

        # 결과에 따라 디렉토리 이동
        if has_face:
            destination_dir = output_dir_with_face
        else:
            destination_dir = output_dir_without_face

        # 이미지를 목적지 디렉토리로 이동
        destination_path = os.path.join(destination_dir, image_file)
        print("destination_path = " + destination_path)
        os.rename(image_path, destination_path)


if __name__ == "__main__":
    print("Start Face Detection...")
    # 환경 변수에서 input 디렉토리 경로 가져오기
    input_directory = os.getenv("INPUT_DIRECTORY", "/app/input_images")
    print("input_directory = " + input_directory)

    process_images(input_directory)

    print("Finished Face Detection...")
