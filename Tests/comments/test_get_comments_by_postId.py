import requests
from Helpers.dataHelper import DataHelper
from TestData import paths, routes

class TestGetSpecificComment:

    # get valid data for valid post Id
    def test_get_specific_comment(self):
        PARAMS = {'postId': 1}
        response = requests.get(url= routes.get_comments_by_post_id, params=PARAMS)
        response_body = response.json()
        assert response.status_code == 200

        # initiate the data helper
        data_helper = DataHelper(paths.comments_by_post_id_json_path, 'comments', PARAMS, -1)

        # compare data
        compare_data = data_helper.compare_expected_with_actual(response_body)




