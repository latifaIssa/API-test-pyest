import json
import requests

from Helpers.dataHelper import DataHelper
from Helpers.jsonHelper import jsonHelper
from TestData import paths
from conftest import base_url

route = f"{base_url}/posts/"

class TestGetSpecificPost:

    # get valid data for id=1
    def test_get_specific_post(self):
        self.id = 1
        response = requests.get(url= route + str(self.id))
        response_body = response.json()
        assert response.status_code == 200

        # get the expected posts
        expected_posts = DataHelper.get_expected(paths.posts_json_path)

        # return the expected post by id
        expected_post = expected_posts['posts'][self.id - 1]

        # Comparing the expected with actual
        assert response_body['id'] == expected_post['id']
        assert response_body["userId"] == expected_post["userId"]
        assert response_body["title"] == expected_post["title"]
        assert response_body["body"] == expected_post["body"]



    # get data for invalid id
    def test_get_specific_post_by_invalid_id(self):
        self.id = 150
        response = requests.get(url= route+str(self.id))
        response_body = response.json()
        assert response.status_code == 404

