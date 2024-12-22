from flask import Blueprint, request, jsonify
from app.sam2_utils import process_image
from app.image_utils import create_outputs, image_to_base64
from PIL import Image as PILImage
import base64
import io

preprocess_blueprint = Blueprint("preprocess", __name__)

@preprocess_blueprint.route('/preprocess', methods=['POST'])
def preprocess():
    data = request.get_json()

    if not data or 'image' not in data:
        return jsonify({"message": "No image provided", "status": "error"}), 400

    try:
        base64_image = data['image']
        image_data = base64.b64decode(base64_image)
        image = PILImage.open(io.BytesIO(image_data)).convert("RGB")

        input_point = data.get("input_point")
        top_mask, top_score = process_image(image, input_point)

        outputs = create_outputs(image, top_mask)

        response_data = {
            key: image_to_base64(img, format="JPEG")
            for key, img in outputs.items()
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"message": "Failed to process image", "error": str(e), "status": "error"}), 500
