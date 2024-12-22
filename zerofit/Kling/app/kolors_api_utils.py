import requests
from config import API_BASE_URL, MODEL_NAME

def create_virtual_tryon_task(api_token, human_image_base64, cloth_image_base64):
    url = f"{API_BASE_URL}/kolors-virtual-try-on"

    data = {
        "model_name": MODEL_NAME,
        "human_image": human_image_base64,
        "cloth_image": cloth_image_base64
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data["data"]["task_id"]
    return None

def get_virtual_tryon_result(api_token, task_id):
    url = f"{API_BASE_URL}/kolors-virtual-try-on/{task_id}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if response_data["data"]["task_status"] == "succeed":
            return response_data["data"]["task_result"]["images"][0]["url"]
    return None
