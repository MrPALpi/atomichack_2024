import io
import json
import time
from io import BytesIO

import requests
from PIL import Image


def run_app():
    while True:
        response = requests.get("http://atomic-hack-fast-api:5000/api/attachment/")
        data = json.loads(response.content)

        if len(data):
            time.sleep(5)

        for attachment_id in data:
            response = requests.get(f"http://atomic-hack-fast-api:5000/api/attachment/{attachment_id}")
            image_data = BytesIO(response.content)
            im = Image.open(image_data)
            # add_predict
            predict_img = im
            imgByteArr = io.BytesIO()
            predict_img.save(imgByteArr, format=predict_img.format)
            imgByteArr = imgByteArr.getvalue()

            response = requests.post(
                f"http://atomic-hack-fast-api:5000/api/yolo/upload-result",
                data={'id': attachment_id},
                files={'file': imgByteArr}
            )
            print(response.content)
        # exit()


if __name__ == "__main__":
    run_app()
