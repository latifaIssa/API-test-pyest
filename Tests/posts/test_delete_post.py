import requests

from TestData import routes

class TestDeletePost:

    # Delete a post by valid id
    def test_delete_post(self):
        self.id = 100
        response = requests.delete(url=routes.get_posts + str(self.id))
        assert response.status_code == 200
        assert response.text == "{}"

    # Delete a post by invalid id
    def test_delete_post_by_invalid_id(self):
        self.id = 200
        response = requests.delete(url=routes.get_posts + str(self.id))
        assert response.status_code == 200 # should be 404?
        assert response.text == "{}"




