import io
import base64
import numpy as np
from PIL import Image as PILImage

def image_to_base64(image, format="JPEG"):
    buffered = io.BytesIO()
    image.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def create_outputs(image, mask):
    cloth_array = np.array(image) * mask[:, :, None]
    cloth_array[mask == 0] = [255, 255, 255]
    cloth = PILImage.fromarray(cloth_array.astype(np.uint8))

    return {
        "cloth": cloth,
    }
