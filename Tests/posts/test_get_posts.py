import requests
from Helpers.dataHelper import DataHelper
from TestData import paths
from conftest import base_url

route = f"{base_url}/posts/"

class TestGetPosts:
    def test_get_posts(self):
        # get the response
        response = requests.get(url=route)
        # read the response as JSON
        response_body = response.json()
        assert response.status_code == 200

        # initiate the data helper
        data_helper = DataHelper(paths.posts_json_path, 'posts')

        # compare data
        compare_data = data_helper.compare_expected_with_actual(response_body)








