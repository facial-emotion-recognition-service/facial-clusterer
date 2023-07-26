"""Provides an API for getting facial clusters from isolated images of faces.
"""

from sklearn.cluster import DBSCAN
import numpy as np


class Clusterer:
    def __init__(self):
        pass

    def get_clusters(self, data, include_unidentified_faces=1):
        """
        Args:
        data: List of img_paths and encoded faces.
        include_unidentified_faces: boolean to inlclude unidentified faces
            when returning results.

        Returns:
        Dictionary of people and all image that include that person.
        People are labeled starting from 0.
        -1 means the face was not identifiable. Exclude by setting
        include_unidentified_faces=0
        """

        encodings = [d["encoding"] for d in data]
        img_paths = [d["imagePath"] for d in data]
        cluster = DBSCAN(metric="euclidean", n_jobs=-1)
        cluster.fit(encodings)

        faces = {}
        for idx, label in enumerate(cluster.labels_):
            label = int(label)
            if label in faces.keys():
                faces[label].append(img_paths[idx])
            else:
                faces[label] = [img_paths[idx]]

        if not include_unidentified_faces:
            faces.pop(-1, None)
        return faces
