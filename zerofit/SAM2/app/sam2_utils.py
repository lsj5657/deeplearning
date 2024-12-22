import numpy as np
from sam2.sam2_image_predictor import SAM2ImagePredictor
from config import args

# SAM2 모델 로드
predictor = SAM2ImagePredictor.from_pretrained("facebook/sam2.1-hiera-large")

def process_image(image, input_point=None):
    predictor.set_image(np.array(image))

    width, height = image.size
    if input_point is None:
        pos_x, pos_y = width // 2, height // 2
        neg_x, neg_y = width // 2, height - 50
        input_point = np.array([[pos_x, pos_y], [neg_x, neg_y]])

    input_label = np.array([1, 0])

    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True,
    )

    sorted_ind = np.argsort(scores)[::-1]
    top_mask = masks[sorted_ind[0]]
    top_score = scores[sorted_ind[0]]

    return top_mask, top_score
