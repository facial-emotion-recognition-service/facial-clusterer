from app_config_provider import AppConfigProvider
from args_provider import ArgsProvider
from app_logic import AppLogic

if __name__ == "__main__":
    appConfigProvider = AppConfigProvider()
    app_config = appConfigProvider.app_config
    argsProvider = ArgsProvider()

    input_faces = app_config["input_faces"]
    json_output_dir = app_config["json_output_dir"]

    args = argsProvider.getArgs()

    app = AppLogic(input_faces, json_output_dir)
    app.get_clusters(args.include_unidentified_faces)
