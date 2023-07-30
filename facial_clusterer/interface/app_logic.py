import json
from pathlib import Path
from facial_clusterer.core.encoder import Encoder
from facial_clusterer.core.clusterer import Clusterer


class AppLogic:
    def __init__(self, input_faces_dir, json_output_dir):
        self.input_faces_dir = Path(input_faces_dir)
        self.json_output_dir = Path(json_output_dir)
        self.encoder = Encoder()

        self.clusterer = Clusterer()

    def get_clusters(self, include_unidentified_faces=1):
        encodings = self.encoder.get_encodings(self.input_faces_dir)
        result = self.clusterer.get_clusters(
            encodings, include_unidentified_faces
        )
        print(result)

        json_str = json.dumps(result, indent=4)
        json_filename = "clusters.json"
        json_file_path = Path(self.json_output_dir, json_filename)
        with open(json_file_path, "w") as f:
            f.write(json_str)
