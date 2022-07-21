import requests

from Helpers.csvHelper import CsvHelper
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest

from conftest import base_url


@ddt
class TestDeletePost(unittest.TestCase):
    # initiate the csv helper
    csv_helper = CsvHelper(paths.delete_post)

    # get data with delete method
    delete_data = csv_helper.get_delete_data()

    @data(*delete_data)
    @unpack
    def test_delete_posts(self, route, headers, query, body, expected, status_code,
                       testcase_title, testcase_description, testcase_severity, testcase_tag):
        # replace the id string with test_id to the route
        new_route = route.replace('id', headers)
        # get the response
        response = requests.delete(url=base_url + new_route)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected)

