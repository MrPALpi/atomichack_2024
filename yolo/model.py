import os
import cv2
import json
from ultralytics import YOLOv10

class YOLODetection:
    def __init__(self, src_folder, results_folder, cm_per_frame, cm_per_sec, model_type='small'):
        self.src_folder = src_folder
        self.results_folder = results_folder
        self.cm_per_frame = cm_per_frame
        self.cm_per_sec = cm_per_sec
        self.model = self._get_model(model_type)
        os.makedirs(results_folder, exist_ok=True)

    def _get_model(self, model_type):
        if model_type == 'nano':
            print('nano model is not available. Using small model instead.')
            # return YOLOv10('weights/yolov10n.pt')
            return YOLOv10('weights/yolov10s.pt')
        elif model_type == 'small':
            return YOLOv10('weights/yolov10s.pt')
        elif model_type == 'medium':
            print('medium model is not available. Using small model instead.')
            return YOLOv10('weights/yolov10s.pt')
            # return YOLOv10('weights/yolov10m.pt')
        else:
            raise ValueError('Invalid model type. Choose from [nano, small, medium]')
        
    def detect_images(self):
        image_folder = os.path.join(self.src_folder)
        result_image_folder = os.path.join(self.results_folder, 'images')
        os.makedirs(result_image_folder, exist_ok=True)
        
        for image_file in os.listdir(image_folder):
            if image_file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(image_folder, image_file)
                image = cv2.imread(image_path)
                results = self.model.predict(image)[0]
                self._save_image_results(image, results, result_image_folder, image_file)

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
                # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # TODO: do we need it?
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
                    
                    results = self.model.predict(frame)[0]
                    self._save_frame_results(frame, results, timestamp, defect_list, lower_coord, upper_coord)

                    out.write(frame)
                    frame_count += 1

                cap.release()
                out.release()
                self._save_defect_list(defect_list, result_video_folder, video_file)
    
    def _save_image_results(self, image, results, folder, file_name):
        for result in results:
            x1, y1, x2, y2 = map(int, result.boxes.xyxy.numpy()[0])
            cls = int(result.boxes.cls.numpy()[0])
            conf = float(result.boxes.conf.numpy()[0])
            label = f'{result.names[cls]} {conf:.2f}'
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        save_path = os.path.join(folder, file_name)
        cv2.imwrite(save_path, image)

    def _save_frame_results(self, frame, results, timestamp, defect_list, lower_coord, upper_coord):
        for result in results:
            x1, y1, x2, y2 = map(int, result.boxes.xyxy.numpy()[0])
            cls = int(result.boxes.cls.numpy()[0])
            conf = float(result.boxes.conf.numpy()[0])
            label = f'{result.names[cls]} {conf:.2f}'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            defect_list.append({
                'class': result.names[cls],
                'coordinates': {
                    'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2
                },
                'timestamp': timestamp,
                'lower_coord': lower_coord,
                'upper_coord': upper_coord
            })

    def _save_defect_list(self, defect_list, folder, file_name):
        result_file_path = os.path.join(folder, f'{os.path.splitext(file_name)[0]}_defects.json')
        with open(result_file_path, 'w') as f:
            json.dump(defect_list, f, indent=4)

def example(id = 1):
    src_folder = f'task/{id}/src'
    results_folder = f'task/{id}/results'
    model_type = 'small'
    cm_per_frame = 50
    cm_per_sec = 10

    yolo_detector = YOLODetection(src_folder, results_folder, cm_per_frame, cm_per_sec, model_type)
    yolo_detector.detect_images()
    # yolo_detector.detect_videos() # TODO: test video detection

if __name__ == '__main__':
    example()