import requests
from conftest import base_url
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest


@ddt
class TestGetPosts(unittest.TestCase):
    # initiate the csv helper
    json_helper = JsonHelper(paths.posts_json_path)

    # get data with get method
    get_data = json_helper.get_get_data()

    @data(*get_data)
    @unpack
    def test_get_posts(self, route, request, status_code, body, sevirty, title, expected):
        # get the response
        response = requests.get(url=base_url + route)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected)


