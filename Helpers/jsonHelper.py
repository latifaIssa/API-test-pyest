import os
import conftest

class jsonHelper:
    @staticmethod
    def get_path(path):
        if "fromTerminal" in os.environ and os.environ["fromTerminal"] != "":
            return path
        else:
            return f'../../{path}'

