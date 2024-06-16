import os
import time
import pandas as pd
from PIL import Image
from model import YOLODetection

yolo_detector = YOLODetection()

test_path = 'dataset'
results = {
    "filename": [],
    "class_id": [],
    "rel_x": [],
    "rel_y": [],
    "width": [],
    "height": []
}

start_time = time.time()
for image_file in os.listdir(test_path):
    if image_file.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(test_path, image_file)
        image = Image.open(image_path)
        
        result_image, detections = yolo_detector._process_image(image)

        image_width, image_height = image.size

        for detection in detections:
            x1, y1, x2, y2 = detection['bbox'].values()
            class_id = detection['class_id']
            rel_x = (x1 + x2) / 2 / image_width
            rel_y = (y1 + y2) / 2 / image_height
            width = (x2 - x1) / image_width
            height = (y2 - y1) / image_height

            results["filename"].append(image_file)
            results["class_id"].append(class_id)
            results["rel_x"].append(rel_x)
            results["rel_y"].append(rel_y)
            results["width"].append(width)
            results["height"].append(height)

end_time = time.time()
inference_time = end_time - start_time
print(f"Time elapsed: {inference_time}")
for key, value in results.items():
    print(f"Length of {key}: {len(value)}")
df = pd.DataFrame(results)
df.to_csv("submission.csv", index=False, sep=";")