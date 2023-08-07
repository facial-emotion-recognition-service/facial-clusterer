import argparse


class ArgsProvider:
    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser()
        # Define command-line arguments and options using argparse
        parser.add_argument(
            "--faces_dir",
            type=str,
            help="directory containing face images to cluster",
        )
        parser.add_argument(
            "--include_unidentified_faces",
            default=1,
            type=int,
            help="boolean to inlclude unidentified faces when returning results",
        )
        args = parser.parse_args()
        return args
