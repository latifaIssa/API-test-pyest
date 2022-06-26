import requests
import json
import jsonpath
# from TestData import posts
from requests.exceptions import HTTPError

baseUrl = "https://jsonplaceholder.typicode.com/"
route = "https://jsonplaceholder.typicode.com/posts/"

class TestPost:


    def test_post_posts(self):
        data={
            "title" : "this new post",
            "body": "this new post",
            "userId": 101
        }
        response = requests.post(url=route, data= data)
        response_body = response.json()
        # extracting response text
        pastebin_url = response.text
        print("The pastebin URL is:%s" % pastebin_url)
