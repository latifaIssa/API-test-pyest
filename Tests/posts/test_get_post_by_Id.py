import requests
from Helpers.dataHelper import DataHelper
from TestData import paths, routes


class TestGetSpecificPost:

    # get valid data for id=1
    def test_get_specific_post(self):
        self.id = 1
        response = requests.get(url=routes.get_posts + str(self.id))
        response_body = response.json()
        assert response.status_code == 200

        # initiate the data helper
        data_helper = DataHelper(paths.posts_json_path, 'posts', {}, self.id)

        # compare data
        response_list = []
        response_list.append(response_body)
        compare_data = data_helper.compare_expected_with_actual(response_list)

    # get data for invalid id
    def test_get_specific_post_by_invalid_id(self):
        self.id = 150
        response = requests.get(url=routes.get_posts + str(self.id))
        response_body = response.json()
        assert response.status_code == 404
