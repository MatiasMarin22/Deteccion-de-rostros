import cv2
import os
from datetime import datetime


FOTOS_DIR = "Fotos"
if not os.path.exists(FOTOS_DIR):
    os.makedirs(FOTOS_DIR)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_face(frame, face_id):
    """Captura y guarda la foto de un rostro detectado."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    photo_path = os.path.join(FOTOS_DIR, f"rostro_{face_id}_{timestamp}.jpg")
    cv2.imwrite(photo_path, frame)
    print(f"Foto guardada en: {photo_path}")

def main():
    cap = cv2.VideoCapture(0)
    face_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_roi = frame[y:y + h, x:x + w]
            capture_face(face_roi, face_id)

        cv2.imshow('Detección de Rostros', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
