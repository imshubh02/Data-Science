import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import cv2

path = 'Mini_Project/blaze_face_short_range.tflite'

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
FaceDetectorResult = mp.tasks.vision.FaceDetectorResult
VisionRunningMode = mp.tasks.vision.RunningMode

results = []
# Create a face detector instance with the live stream mode:
def process_result(result: FaceDetectorResult, output_image: mp.Image, timestamp_ms: int):
    results.append(result)

options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path=path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=process_result)
with FaceDetector.create_from_options(options) as detector:
    print("Face detection model loaded")
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        state, image = cam.read()
        if not state: break
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        ts = int(time.time() * 1000)
        detector.detect_async(mp_image, ts)