import json

import requests

from Helpers.csvHelper import CsvHelper
from conftest import base_url
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest



@ddt
class TestGetPosts(unittest.TestCase):
    # initiate the csv helper
    csv_helper = CsvHelper(paths.posts_json_path)

    # get data with get method
    get_data = csv_helper.get_get_data()

    @data(*get_data)
    @unpack
    def test_get_posts(self, route, headers, query, body, expected, status_code,
                                   testcase_title, testcase_description, testcase_severity, testcase_tag):
        # get the response
        response = requests.get(url=base_url + route)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # Convert the expected text to json
        expected_result = JsonHelper.get_json(expected)

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected_result)


