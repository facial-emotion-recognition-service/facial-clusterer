import os
import face_recognition
import json

directory_str = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/frames"
directory = os.fsencode(directory_str)

output = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/coords/coords.json"

with open(output, "r") as outfile:
    data = json.load(outfile)


faces = {}

for file in data.keys():
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        img_path = os.path.join(directory_str, filename)
        coords[filename] = extractor.extract_faces(img_path)
        continue
    else:
        continue

for i, imagePath in enumerate(imagePaths):
    # load the input image and convert it from RGB (OpenCV ordering)
    # to dlib ordering (RGB)
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    print(imagePath)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
