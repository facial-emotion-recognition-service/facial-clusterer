"""Provides an API for getting facial clusters from isolated images of faces.
"""

from sklearn.cluster import DBSCAN


class Clusterer:
    def __init__(self):
        pass

    def get_clusters(self, data, include_unidentified_faces=1):
        encodings = [d["encoding"] for d in data]
        img_paths = [d["imagePath"] for d in data]
        cluster = DBSCAN(metric="euclidean", n_jobs=-1)
        cluster.fit(encodings)

        faces = {}
        for idx, label in enumerate(cluster.labels_):
            if label in faces.keys():
                faces[label].append(img_paths[idx])
            else:
                faces[label] = [img_paths[idx]]

        if not include_unidentified_faces:
            faces.pop(-1, None)
        return faces
