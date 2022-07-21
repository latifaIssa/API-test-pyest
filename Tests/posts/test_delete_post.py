import requests

from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest

from conftest import base_url


@ddt
class TestDeletePost(unittest.TestCase):
    # initiate the csv helper
    json_helper = JsonHelper(paths.delete_post)

    # get data with delete method
    delete_data = json_helper.get_delete_data()

    @data(*delete_data)
    @unpack
    # Delete a post by valid id
    def test_delete_post(self, route, request, status_code, body, sevirty, title,test_id, expected):
        # replace the id string with test_id to the route
        new_route = route.replace('id', test_id)

        # get the response
        response = requests.delete(url=base_url + new_route)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual([response.json()], [expected])
