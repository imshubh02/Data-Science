import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# For static images:
image_files = []
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
  for idx, file in enumerate(image_files):
    image = cv2.imread(file)
   
    # Convert the BGR image to RGB image
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
      continue
    annotated_image = image.copy()
    for detection in results.detections:
      print(mp_face_detection.get_key_point(
          detection, mp_face_detection.FaceKeyPoint.MOUTH))
      mp_drawing.draw_detection(annotated_image, detection)
    
# For webcam input:
cam = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cam.isOpened():
    success, image = cam.read()
    if not success:
      continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)
  
    # Draw the face detection annotations on the image.
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    
    cv2.imshow('MediaPipe Face Detection', image)
    key = cv2.waitKey(10)
    if key == 27: 
      break

cam.release()
cv2.destroyAllWindows()