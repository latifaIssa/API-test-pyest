import requests
import json
from Helpers.jsonHelper import jsonHelper
from TestData import paths

route = "https://jsonplaceholder.typicode.com/posts/"

class TestGetPosts:
    def test_get_posts(self):
        # get the response
        response = requests.get(url=route)
        # read the response as JSON
        response_body = response.json()
        assert response.status_code == 200

        # Opening JSON file
        expected_json = open(jsonHelper.get_path(paths.posts_json_path))

        # returns JSON object as  a dictionary
        expected_posts = json.load(expected_json)

        # Iterating through the json list
        for index, post in enumerate(expected_posts['posts']):
            assert response_body[index]['id'] == post['id']
            assert response_body[index]["userId"] == post["userId"]
            assert response_body[index]["title"] == post["title"]
            assert response_body[index]["body"] == post["body"]

        # Closing file
        expected_json.close()






