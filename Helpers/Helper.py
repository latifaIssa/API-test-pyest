import os


class Helper:

    @staticmethod
    def get_path(path):
        if "fromTerminal" in os.environ and os.environ["fromTerminal"] != "":
            return path
        else:
            return f'../../{path}'


    @staticmethod
    def get_classification():
        if "classification" in os.environ:
            return os.environ['classification'].lower()
        else:
            return ""
