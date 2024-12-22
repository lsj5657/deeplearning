from flask import Blueprint, request, jsonify
from app.jwt_utils import encode_jwt_token
from app.kolors_api_utils import create_virtual_tryon_task
from app.image_utils import wait_for_task_completion, image_url_to_base64

kolors_blueprint = Blueprint("kolors", __name__)

@kolors_blueprint.route('/kolors', methods=['POST'])
def virtual_tryon():
    try:
        data = request.json
        person_base64 = data["person"]
        cloth_base64 = data["cloth"]

        api_token = encode_jwt_token()
        task_id = create_virtual_tryon_task(api_token, person_base64, cloth_base64)

        if not task_id:
            return jsonify({"error": "Failed to create task"}), 400

        result_url = wait_for_task_completion(api_token, task_id)

        if not result_url:
            return jsonify({"error": "Failed to retrieve task result"}), 400

        result_base64 = image_url_to_base64(result_url)

        if not result_base64:
            return jsonify({"error": "Failed to convert result image to Base64"}), 500

        return jsonify({"result": result_base64}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
