"""Provides an API for getting encodings for isolated images of faces.
"""

import os
import cv2
import face_recognition


class Encoder:
    def __init__(self):
        pass

    def get_encoding(self, img_path):
        """Get encoding for a single image."""
        img = cv2.cvtColor(
            cv2.imread(img_path), cv2.COLOR_BGR2RGB
        )  # since we're not displaying the image, is the encoding impacted by color?
        h, w, _ = img.shape
        coords = [(0, w, h, 0)]

        encoding = face_recognition.face_encodings(img, coords)
        # build a dictionary of the image path, bounding box location,
        # and facial encoding
        d = {"imagePath": img_path, "encoding": encoding[0]}

        return d

    def get_encodings(self, dir_):
        """Get encodings for all images in a directory"""
        encodings = []
        for file in os.listdir(dir_):
            filename = os.fsdecode(file)
            img_path = os.path.join(dir_, filename)
            encoding = self.get_encoding(img_path)
            encodings.append(encoding)

        return encodings


if __name__ == "__main__":
    dir_ = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/face/"
    encoder = Encoder()
    print(encoder.get_encodings(dir_))
