import requests
import os
import io
from PIL import Image
import base64
import json


# 서버 URL 및 이미지 경로 설정
#url = "http://165.246.21.212:10103/preprocess"
url = "http://192.168.0.7:10103/preprocess"
#image_path = "sam/images/img0004.jpg"
image_path = "cloth/img2.jpg"

# 저장 디렉토리 설정
save_dir = "results"


# 디렉토리가 없으면 생성
os.makedirs(save_dir, exist_ok=True)

# 이미지 파일을 Base64로 변환
with open(image_path, "rb") as f:
    base64_image = base64.b64encode(f.read()).decode('utf-8')
data = {
    "image": base64_image
}

# Optional: 좌표 추가

input_point = [[660,500], [0, 0]]  # 예시 좌표
# if input_point:  # 조건에 따라 좌표를 추가
#     data["input_point"] = input_point

#print(data)

# POST 요청 보내기
headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, data=json.dumps(data))

#print(data['input_point'])

if response.status_code == 200:
    # 원본 이미지 이름 추출
    response_data = response.json()
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # 서버에서 반환된 이미지를 저장
    for key, base64_data in response_data.items():
        # Base64 디코딩
        img_data = base64.b64decode(base64_data)
        img = Image.open(io.BytesIO(img_data))

        if key == "cloth":
            save_path = os.path.join(save_dir, f"{base_name}.jpg")
        else:
            continue  # 알 수 없는 키는 무시
        
        
        print(f"save_path = {save_path}")
        # 이미지 저장
        img.save(save_path)
        print(f"Saved: {save_path}")

else:
    print("Error:", response.json())