import json
from Helpers.Helper import Helper


class JsonHelper:

    def __init__(self, path):
        # Opening JSON file
        self.test_data_json = open(Helper.get_path(path))

        # returns JSON object as  a dictionary
        self.test_data_dict = json.load(self.test_data_json)

        # return a list of values
        self.test_data = self.test_data_dict.values()

        # Closing file
        self.test_data_json.close()

    def __get_data(self, method):
       values_list = list(filter(lambda x: x["request"] == method, self.test_data))
       return values_list

    def get_post_data(self):
        return self.__get_data('post')

    def get_all_data(self):
        return self.test_data

    def get_get_data(self):
        return self.__get_data('get')

    def get_put_data(self):
        return self.__get_data('put')

    def get_patch_data(self):
        return self.__get_data('patch')

    def get_delete_data(self):
        return self.__get_data('delete')

