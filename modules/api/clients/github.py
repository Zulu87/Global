
import requests


class GitHub:

    def get_user(self, username):
        req = requests.get(f"https://api.github.com/users/{username}")
        body = req.json()
        return body

    def search_repo(self, name):
        req = requests.get("https://api.github.com/search/repositories", params = {"q" : name})
        body = req.json()
        return body