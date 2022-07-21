import requests

from conftest import base_url
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest

@ddt
class TestAddPost(unittest.TestCase):
    # initiate the csv helper
    json_helper = JsonHelper(paths.add_post)

    # get data with post method
    post_data = json_helper.get_post_data()

    @data(*post_data)
    @unpack

    # valid body data
    def test_add_post(self, route, request, status_code, body, sevirty, title, test_data, expected):
        # get the response
        response = requests.post(url=base_url + route, json=test_data)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected)
