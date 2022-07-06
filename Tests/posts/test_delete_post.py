import requests
import json

route = "https://jsonplaceholder.typicode.com/posts/"

class TestDeletePost:

    # Delete a post by valid id
    def test_delete_post(self):
        self.id = 100
        response = requests.delete(url=route + str(self.id))
        print(response)
        assert response.status_code == 200
        assert response.text == "{}"

    # Delete a post by invalid id
    def test_delete_post_by_invalid_id(self):
        self.id = 200
        response = requests.delete(url=route + str(self.id))
        print(response)
        assert response.status_code == 404
        assert response.text == "{}"




