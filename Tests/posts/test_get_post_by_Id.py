import requests
import json
import jsonpath
# from TestData import posts
from requests.exceptions import HTTPError

baseUrl = "https://jsonplaceholder.typicode.com/"
route = "https://jsonplaceholder.typicode.com/posts/ "
class TestGetSpecificPost:

    # get valid data for id=1
    def test_get_specific_post(self):
        self.id = 1
        response = requests.get(url= route + str(self.id))
        response_body = response.json()
        assert response.status_code == 200
        assert response_body["id"] == 1
        assert response_body["userId"] == 1
        assert response_body["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
        assert response_body ["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

    #get data for invalid id
    def test_get_specific_post(self):
        self.id = 150
        response = requests.get(url= route+str(self.id))
        response_body = response.json()
        assert response.status_code == 404

