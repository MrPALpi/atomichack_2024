import io
import json
import time
from io import BytesIO

import requests
from PIL import Image

import model


def run_app():
    model_type = 'small'
    cm_per_frame = 50
    cm_per_sec = 10

    yolo_detector = model.YOLODetection(cm_per_frame, cm_per_sec, model_type)

    while True:
        response = requests.get("http://atomic-hack-fast-api:5000/api/attachment/")
        data = json.loads(response.content)

        if len(data):
            time.sleep(5)

        for attachment_id in data:
            response = requests.get(f"http://atomic-hack-fast-api:5000/api/attachment/{attachment_id}")
            image_data = BytesIO(response.content)
            im = Image.open(image_data)
            
            #получение дефекта
            predict_img, tags = yolo_detector._process_image(im)

            imgByteArr = io.BytesIO()
            # format=predict_img.format
            predict_img.save(imgByteArr, format=im.format)
            imgByteArr = imgByteArr.getvalue()

            tags_r = [None,]

            for tag in tags:
                tag_class = tag.get('class', None)
                if tag_class is not None:
                    tags_r.append(tag_class)

            response = requests.post(
                f"http://atomic-hack-fast-api:5000/api/yolo/upload-result",
                data={'id': attachment_id, 'tags': tags_r},
                files={'file': imgByteArr}
            )
            print(response.content)


if __name__ == "__main__":
    run_app()
