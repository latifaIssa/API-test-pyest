import requests

from TestData import routes


class TestPostPosts:

    # valid body data
    def test_post_posts(self):
        data = {
            "title": "this new post",
            "body": "this new post",
            "userId": "101"
        }
        response = requests.post(routes.get_posts, json=data)
        response_body = response.json()
        assert response.status_code == 201

    # invalid body data
    def test_post_posts_invalid_data(self):
        data = {

        }
        response = requests.post(routes.get_posts, json=data)
        response_body = response.json()
        assert response.status_code == 201
        print(response_body)
