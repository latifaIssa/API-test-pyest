import requests
import json
import jsonpath
# from TestData import posts
from requests.exceptions import HTTPError

baseUrl = "https://jsonplaceholder.typicode.com/"
route = "https://jsonplaceholder.typicode.com/comments/"

class TestGetSpecificPost:

    # get valid data for id=1
    def test_get_specific_comment(self):
        PARAMS = {'postId': 1}
        response = requests.get(url= route, params=PARAMS)
        response_body = response.json()
        assert response.status_code == 200
        # assert response_body["id"] == 1
        # assert response_body["name"] == "id labore ex et quam laborum"
        # assert response_body["email"] == "Eliseo@gardner.biz"
        # assert response_body ["body"] == "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"



