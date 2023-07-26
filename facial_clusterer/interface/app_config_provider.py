import os


class AppConfigProvider:
    def __init__(self):
        self._input_faces = os.path.join(
            os.environ.get("IMAGE_INPUT_DIR", "../input_images/"), "faces"
        )
        self._json_output_dir = os.environ.get(
            "JSON_OUTPUT_DIR", "../output_json/"
        )

    @property
    def app_config(self):
        result = {
            "input_faces": self._input_faces,
            "json_output_dir": self._json_output_dir,
        }

        return result
