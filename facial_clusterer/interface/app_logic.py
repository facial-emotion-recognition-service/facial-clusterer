import json
import os
from pathlib import Path
from facial_clusterer.core.encoder import Encoder
from facial_clusterer.core.clusterer import Clusterer


class AppLogic:
    def __init__(self, image_input_dir, json_output_dir):
        self.image_input_dir = Path(image_input_dir)
        self.json_output_dir = Path(json_output_dir)
        self.encoder = Encoder()

        self.clusterer = Clusterer()

    def get_clusters(self, faces_dir, include_unidentified_faces=1):
        input_faces_dir = os.path.join(self.image_input_dir, faces_dir)
        encodings = self.encoder.get_encodings(input_faces_dir)
        result = self.clusterer.get_clusters(
            encodings, include_unidentified_faces
        )
        print(result)

        json_str = json.dumps(result, indent=4)
        json_filename = "clusters.json"
        json_file_path = Path(self.json_output_dir, json_filename)
        with open(json_file_path, "w") as f:
            f.write(json_str)
