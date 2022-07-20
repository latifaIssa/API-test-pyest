import json

import requests

from Helpers.jsonHelper import JsonHelper
from TestData import paths


class DataHelper:

    def __init__(self, path, name='', paramsRequest={}, i=-1):
        # Opening JSON file
        self.expected_json = open(JsonHelper.get_path(path))

        # returns JSON object as  a dictionary
        self.expected_posts = json.load(self.expected_json)

        # get the list of object
        self.items_list = self.expected_posts[name]

        # return the expected item by id
        if (i > -1):
            expected_item = self.items_list[i - 1]
            self.items_list = []
            self.items_list.append(expected_item)

        # return the expected items according to specific condition
        if (paramsRequest != {}):
            get_key = paramsRequest.keys()
            for key in get_key:
                expected_items_by_id = list(filter(lambda x: x[key] == paramsRequest[key], self.items_list))
            self.items_list = expected_items_by_id

        # get object's keys
        if (len(self.items_list) > 0):
            self.keys = self.items_list[0].keys()

        # Closing file
        self.expected_json.close()

    def compare_expected_with_actual(self, actual):
        # Iterating through the json list
        for index, item in enumerate(self.items_list):
            for key in self.keys:
                assert actual[index][key] == item[key]
