import unittest

import requests
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack

from conftest import base_url


@ddt
class TestGetSpecificPost(unittest.TestCase):
    # initiate the csv helper
    json_helper = JsonHelper(paths.get_post_by_id)

    # get all the data
    get_data = json_helper.get_get_data()

    @data(*get_data)
    @unpack
    # get valid data for id=1
    def test_get_specific_post(self, route, request, status_code, body, sevirty, title,test_id, expected):
        # replace the id string with test_id to the route
        new_route = route.replace('id', test_id)

        # get the response
        response = requests.get(url=base_url + new_route)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual([response.json()], [expected])



