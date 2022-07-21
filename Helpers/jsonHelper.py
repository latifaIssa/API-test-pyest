import json


class JsonHelper:

    @staticmethod
    def get_json(data):
        result = json.loads(data.replace("\n", ''))
        return result
