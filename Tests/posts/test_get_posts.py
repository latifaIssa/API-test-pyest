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



        #get the expected posts
        expected_posts = DataHelper.get_expected(paths.posts_json_path)

        # Iterating through the json list
        for index, post in enumerate(expected_posts['posts']):
            assert response_body[index]['id'] == post['id']
            assert response_body[index]["userId"] == post["userId"]
            assert response_body[index]["title"] == post["title"]
            assert response_body[index]["body"] == post["body"]







