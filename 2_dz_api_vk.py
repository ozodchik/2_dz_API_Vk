from urllib.parse import urljoin
import requests


TOKEN_1 = "some token"
TOKEN_2 = "some token"
V = "5.214"
API_BASE_URL = "https://api.vk.com/method/"


class User:
    BASE_URL = API_BASE_URL

    def __init__(self, token=TOKEN, version=V):
        self.token = token
        self.version = version

    def get_user_friends(self):
        link = urljoin(API_BASE_URL, "friends.get")
        res = requests.get(link, params={"access_token": self.token, "v": self.version})
        result = res.json()
        if res.status_code != 200:
            raise Exception(f"ошибка! \n код ошибки {res.status_code}")
        return result


    def __and__(self, other):
        argument_1 = self.get_user_friends()
        result_1 = set(argument_1["response"]["items"])
        argument_2 = other.get_user_friends()
        result_2 = set(argument_2["response"]["items"])
        set_result = result_1.intersection(result_2)
        return f'список общих друзей: \n {list(set_result)}'



if __name__ == "__main__":
    first = User(TOKEN_1, V)
    second = User(TOKEN_2, V)
    print(first.get_user_friends())
    print(second.get_user_friends())
    print((first & second))
