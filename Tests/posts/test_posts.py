import requests
import json
import jsonpath
# from TestData import posts
from requests.exceptions import HTTPError

baseUrl = "https://jsonplaceholder.typicode.com/"
route = "https://jsonplaceholder.typicode.com/posts/"

class TestPost:
    def test_get_posts(self):
        response = requests.get(url=route)
        response_body = response.json()
        assert response.status_code == 200
        with open("TestData/posts.json") as jsonFile:
            expected_posts = json.load(jsonFile)
            # jsonFile.close()

        assert len(response_body) == 100
        for index, post in enumerate(expected_posts['posts']):
            print (post)
            # assert response_body["id"][index] == post.userId
            # assert response_body["userId"][index] == post.id
            # assert response_body["title"][index] == post.title
            # assert response_body["body"][index] == post.body


    def delete_post(self):
        self.id = 1
        response = requests.delete(url=route + str(self.id))
        print(response.text)
        assert response.text == "One record deleted"



