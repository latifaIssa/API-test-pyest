import json

import requests

from Helpers.jsonHelper import jsonHelper
from TestData import paths


class DataHelper:

    @staticmethod
    def get_expected(path):
        # Opening JSON file
        expected_json = open(jsonHelper.get_path(path))

        # returns JSON object as  a dictionary
        expected_posts = json.load(expected_json)

        # Closing file
        expected_json.close()
        return expected_posts

