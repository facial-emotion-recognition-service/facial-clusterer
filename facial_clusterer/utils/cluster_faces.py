from sklearn.cluster import DBSCAN
import numpy as np
import pickle
import cv2
import os
from human_emotion.core.predictors import Predictor


COLOR_LIST = [
    (230, 25, 75),
    (60, 180, 75),
    (255, 225, 25),
    (0, 130, 200),
    (245, 130, 48),
    (145, 30, 180),
    (70, 240, 240),
    (240, 50, 230),
    (210, 245, 60),
    (250, 190, 212),
    (0, 128, 128),
    (220, 190, 255),
    (170, 110, 40),
    (255, 250, 200),
    (128, 0, 0),
    (170, 255, 195),
    (128, 128, 0),
    (255, 215, 180),
    (0, 0, 128),
    (128, 128, 128),
    (255, 255, 255),
    (0, 0, 0),
]

IMG_EXTENSION = ".jpg"
DIRECTORY_STR = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/frames"
DIRECTORY = os.fsencode(DIRECTORY_STR)
OUTPUT_IMAGE = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/working_frames"

PICKLE_OUTPUT = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/coords/coords.json"

ENCODING = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/pickle.pkl"

data = pickle.loads(open(ENCODING, "rb").read())

data = np.array(data)
encodings = [d["encoding"] for d in data]

clt = DBSCAN(metric="euclidean", n_jobs=-1)
clt.fit(encodings)
# determine the total number of unique faces found in the dataset
labelIDs = np.unique(clt.labels_)
numUniqueFaces = len(np.where(labelIDs > -1)[0])


filenames = set([d["imagePath"] for d in data])


for filename in filenames:
    encoding_idx = [
        idx for idx, value in enumerate(data) if value["imagePath"] == filename
    ]

    img_path = os.path.join(DIRECTORY_STR, filename)
    img = cv2.imread(img_path)

    for idx in encoding_idx:
        x1, y1, x2, y2 = data[idx]["loc"]
        face_num = clt.labels_[idx]
        label = f"Face {str(face_num)}"
        color = COLOR_LIST[face_num]
        cv2.rectangle(img, (y2, x1), (y1, x2), color, 2)
        cv2.putText(img, label, (y2, x1 - 10), cv2.FONT_HERSHEY_DUPLEX, 2, color, 2)

    cv2.imwrite(os.path.join(OUTPUT_IMAGE, filename), img)


print("[INFO] # unique faces: {}".format(numUniqueFaces))
