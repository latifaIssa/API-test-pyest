import requests
from Helpers.dataHelper import DataHelper
from TestData import paths
from conftest import base_url
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest

@ddt
class TestGetSpecificComment(unittest.TestCase):
    # initiate the csv helper
    json_helper = JsonHelper(paths.comments_by_post_id_json_path)

    # get data with get method
    get_data = json_helper.get_get_data()

    @data(*get_data)
    @unpack

    # get valid data for valid post Id
    def test_get_specific_comment(self, route, request, status_code, body, sevirty, title,test_params, expected):
        # get the response
        response = requests.get(url=base_url + route, params=test_params)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")
        print(response.json())

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected)
