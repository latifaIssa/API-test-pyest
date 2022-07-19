import json
import requests
from Helpers.jsonHelper import jsonHelper
from TestData import paths

route = "https://jsonplaceholder.typicode.com/comments/"

class TestGetSpecificComment:

    # get valid data for valid post Id
    def test_get_specific_comment(self):
        PARAMS = {'postId': 1}
        response = requests.get(url= route, params=PARAMS)
        response_body = response.json()
        assert response.status_code == 200

        # Opening JSON file
        expected_json = open(jsonHelper.get_path(paths.comments_by_post_id_json_path))

        # returns JSON object as  a dictionary
        expected_comments = json.load(expected_json)

        # return the expected posts by id
        expected_posts_by_postId = list(filter(lambda x: x['postId'] == PARAMS['postId'], expected_comments['comments']))

        # Iterating through the json list
        for index, comment in enumerate(expected_posts_by_postId):
            assert response_body[index]['id'] == comment['id']
            assert response_body[index]["name"] == comment["name"]
            assert response_body[index]["email"] == comment["email"]
            assert response_body[index]["body"] == comment["body"]

        # Closing file
        expected_json.close()



