import os


class AppConfigProvider:
    def __init__(self):
        self._image_input_dir = os.environ.get("IMAGE_INPUT_DIR")
        self._json_output_dir = os.environ.get("JSON_OUTPUT_DIR")

    @property
    def app_config(self):
        result = {
            "image_input_dir": self._image_input_dir,
            "json_output_dir": self._json_output_dir,
        }

        return result
