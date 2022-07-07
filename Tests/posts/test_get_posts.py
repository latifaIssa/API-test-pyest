import requests
import json

route = "https://jsonplaceholder.typicode.com/posts/"

class TestPost:
    def test_get_posts(self):
        # get the response
        response = requests.get(url=route)
        # read the response as JSON
        response_body = response.json()
        assert response.status_code == 200

        # Opening JSON file
        expected_json = open('TestData/posts.json')

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






