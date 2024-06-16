import os
import cv2
import json
import numpy as np
from PIL import Image
from io import BytesIO
from ultralytics import YOLOv10

class YOLODetection:
    def __init__(self, cm_per_frame, cm_per_sec, model_type='small'):
        self.cm_per_frame = cm_per_frame
        self.cm_per_sec = cm_per_sec
        self.model = self._get_model(model_type)

    def _get_model(self, model_type):
        if model_type == 'nano':
            return YOLOv10('weights/yolov10n.pt')
        elif model_type == 'small':
            return YOLOv10('weights/yolov10s.pt')
        elif model_type == 'medium':
            print('medium model is not available. Using small model instead.')
            return YOLOv10('weights/yolov10s.pt')
        else:
            raise ValueError('Invalid model type. Choose from [nano, small, medium]')
        
    def _get_pillow_image(self, cv2_image):
        return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

    def _get_cv2_image(self, pillow_image):
        return cv2.cvtColor(np.array(pillow_image), cv2.COLOR_RGB2BGR)
    
    def detect_images(self):
        image_folder = os.path.join(self.src_folder)
        result_image_folder = os.path.join(self.results_folder, 'images')
        os.makedirs(result_image_folder, exist_ok=True)
        
        for image_file in os.listdir(image_folder):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(image_folder, image_file)
                image = Image.open(image_path)
                result_image, detections = self._process_image(image)
                result_image.save(os.path.join(result_image_folder, image_file))

    def detect_videos(self):
        video_folder = os.path.join(self.src_folder)
        result_video_folder = os.path.join(self.results_folder, 'videos')
        os.makedirs(result_video_folder, exist_ok=True)
        
        for video_file in os.listdir(video_folder):
            if video_file.endswith('.mp4'):
                video_path = os.path.join(video_folder, video_file)
                cap = cv2.VideoCapture(video_path)
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = cap.get(cv2.CAP_PROP_FPS)
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                result_path = os.path.join(result_video_folder, video_file)
                out = cv2.VideoWriter(result_path, fourcc, fps, (width, height))

                frame_count = 0
                defect_list = []

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    timestamp = frame_count / fps
                    lower_coord = self.cm_per_sec * timestamp
                    upper_coord = lower_coord + self.cm_per_frame
                    
                    pillow_frame = self._get_pillow_image(frame)
                    result_image, detections = self._process_image(pillow_frame)
                    defect_list.extend(self._create_defect_list(detections, timestamp, lower_coord, upper_coord))
                    out.write(self._get_cv2_image(result_image))
                    frame_count += 1

                cap.release()
                out.release()
                self._save_defect_list(defect_list, result_video_folder, video_file)
    
    def _process_image(self, image):
        cv2_image = self._get_cv2_image(image)
        results = self.model.predict(cv2_image)[0]
        detections = []

        # Define colors for classes
        class_colors = {
            0: (0, 255, 0),     # Green
            1: (128, 0, 128),   # Purple
            2: (255, 0, 0),     # Red
            4: (0, 0, 255),     # Blue
            5: (255, 165, 0)    # Orange
        }

        for result in results:
            x1, y1, x2, y2 = map(int, result.boxes.xyxy.numpy()[0])
            cls = int(result.boxes.cls.numpy()[0])
            if cls != 3:  # Exclude "line" class (class 3)
                label = f'{result.names[cls]}'
                x_center = (x1 + x2) // 2
                y_center = (y1 + y2) // 2
                detections.append({
                    'class': result.names[cls],
                    'center': {'x': x_center, 'y': y_center}
                })
                color = class_colors.get(cls, (0, 255, 0))  # Default to green if class not in defined colors
                cv2.rectangle(cv2_image, (x1, y1), (x2, y2), color, 2)
                cv2.putText(cv2_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return self._get_pillow_image(cv2_image), detections

    def _create_defect_list(self, detections, timestamp, lower_coord, upper_coord):
        defect_list = []
        for detection in detections:
            defect_list.append({
                'class': detection['class'],
                'center': detection['center'],
                'timestamp': timestamp,
                'lower_coord': lower_coord,
                'upper_coord': upper_coord
            })
        return defect_list

    def _save_defect_list(self, defect_list, folder, file_name):
        result_file_path = os.path.join(folder, f'{os.path.splitext(file_name)[0]}_defects.json')
        with open(result_file_path, 'w') as f:
            json.dump(defect_list, f, indent=4)

def example(id=1):
    src_folder = f'task/{id}/src'
    results_folder = f'task/{id}/results'
    model_type = 'small'
    cm_per_frame = 50
    cm_per_sec = 10

    yolo_detector = YOLODetection(cm_per_frame, cm_per_sec, model_type)
    yolo_detector.src_folder = src_folder
    yolo_detector.results_folder = results_folder
    yolo_detector.detect_images()
    yolo_detector.detect_videos()

# if __name__ == '__main__':
#     example()