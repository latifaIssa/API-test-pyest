import requests
from Helpers.dataHelper import DataHelper
from TestData import paths, routes


class TestGetPosts:
    def test_get_posts(self):
        # get the response
        response = requests.get(url=routes.get_posts)
        # read the response as JSON
        response_body = response.json()
        assert response.status_code == 200

        # initiate the data helper
        data_helper = DataHelper(paths.posts_json_path, 'posts')

        # compare data
        compare_data = data_helper.compare_expected_with_actual(response_body)








