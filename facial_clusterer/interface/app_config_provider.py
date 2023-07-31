import os


class AppConfigProvider:
    def __init__(self):
        self._input_faces_dir = os.path.join(
            os.environ.get("IMAGE_INPUT_DIR"), "faces"
        )
        self._json_output_dir = os.environ.get("JSON_OUTPUT_DIR")

    @property
    def app_config(self):
        result = {
            "input_faces_dir": self._input_faces_dir,
            "json_output_dir": self._json_output_dir,
        }

        return result
