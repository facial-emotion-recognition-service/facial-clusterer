from facial_clusterer.core.clusterer import Clusterer
from facial_clusterer.core.encoder import Encoder

if __name__ == "__main__":
    encoder = Encoder()
    dir_ = "/home/nathan/code/nihonlanguageprocessing/facial-emotion-recognition-service/facial-clusterer/raw_data/face/"
    encoder = Encoder()
    encodings = encoder.get_encodings(dir_)

    clusterer = Clusterer()
    results = clusterer.get_clusters(encodings)
    print(results)
