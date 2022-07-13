import pytest
import requests

route = "https://jsonplaceholder.typicode.com/posts/"

class TestPostPosts:

    # valid body data
    def test_post_posts(self):
        data={
            "title" : "this new post",
            "body": "this new post",
            "userId": "101"
        }
        response = requests.post(route, json=data)
        response_body = response.json()
        assert response.status_code == 201

    # invalid body data
    def test_post_posts_invalid_data(self):
        data={

        }
        response = requests.post(route, json=data)
        response_body = response.json()
        assert response.status_code == 201
        print(response_body)