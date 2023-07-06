from sklearn.cluster import DBSCAN
import numpy as np
import pickle
import cv2
import os

ENCODING = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/pickle.pkl"
DIRECTORY_STR = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/frames"
OUTPUT_IMAGE = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/working_frames"


data = pickle.loads(open(ENCODING, "rb").read())

data = np.array(data)
encodings = [d["encoding"] for d in data]

clt = DBSCAN(metric="euclidean", n_jobs=-1)
clt.fit(encodings)
# determine the total number of unique faces found in the dataset
labelIDs = np.unique(clt.labels_)
numUniqueFaces = len(np.where(labelIDs > -1)[0])

for idx, d in enumerate(data):
    filename = d["imagePath"]
    img_path = os.path.join(DIRECTORY_STR, filename)
    img = cv2.imread(img_path)

    x1, y1, x2, y2 = d["loc"]
    label = f"Face {str(clt.labels_[idx])}"
    cv2.rectangle(img, (y2, x1), (y1, x2), 2)
    cv2.putText(img, label, (y2, x1 - 10), cv2.FONT_HERSHEY_COMPLEX, 2, 255)

    cv2.imwrite(os.path.join(OUTPUT_IMAGE, filename), img)


print("[INFO] # unique faces: {}".format(numUniqueFaces))


"""'
"""
