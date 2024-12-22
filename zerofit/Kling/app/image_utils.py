import requests
import base64
import time

def image_url_to_base64(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode("utf-8")
    return None

def wait_for_task_completion(api_token, task_id, max_retries=10, interval=5):
    from app.kolors_api_utils import get_virtual_tryon_result

    for attempt in range(max_retries):
        result_url = get_virtual_tryon_result(api_token, task_id)
        if result_url:
            return result_url
        time.sleep(interval)
    return None
