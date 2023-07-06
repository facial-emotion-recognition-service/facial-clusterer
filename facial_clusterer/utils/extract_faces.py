import os
import pickle
import facial_extraction.core.extractor as extractor
import face_recognition
import cv2

IMG_EXTENSION = ".jpg"
DIRECTORY_STR = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/frames"
DIRECTORY = os.fsencode(DIRECTORY_STR)
OUTPUT_IMAGE = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/working_frames"

PICKLE_OUTPUT = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/coords/coords.json"

ENCODING = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/pickle.pkl"

extractor = extractor.Extractor()

data = []
face_counter = 0
for file in os.listdir(DIRECTORY):
    filename = os.fsdecode(file)
    if filename.endswith(IMG_EXTENSION):
        img_path = os.path.join(DIRECTORY_STR, filename)
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)

        coords = extractor.extract_faces(img_path)

        encodings = face_recognition.face_encodings(img, coords)
        # build a dictionary of the image path, bounding box location,
        # and facial encodings for the current image
        d = [
            {"imagePath": filename, "loc": box, "encoding": enc}
            for (box, enc) in zip(coords, encodings)
        ]

        data.extend(d)
        # print(filename)

print(face_counter)

with open(ENCODING, "wb") as pick:
    pick.write(pickle.dumps(data))
