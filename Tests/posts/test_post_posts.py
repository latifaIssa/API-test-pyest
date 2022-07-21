import requests

from Helpers.csvHelper import CsvHelper
from conftest import base_url
from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import JsonHelper
from TestData import paths
from ddt import ddt, data, unpack
import unittest

@ddt
class TestAddPost(unittest.TestCase):
    # initiate the csv helper
    csv_helper = CsvHelper(paths.add_post)

    # get data with post method
    post_data = csv_helper.get_post_data()

    @data(*post_data)
    @unpack
    # valid body data
    def test_add_post(self, route, headers, query, body, expected, status_code,
                                   testcase_title, testcase_description, testcase_severity, testcase_tag):
        # get the response
        response = requests.post(url=base_url + route, json=query)

        # assertion
        self.assertEqual(status_code, str(response.status_code), "Status code is invalid")

        # compare data
        DataHelper.compare_expected_with_actual(response.json(), expected)
