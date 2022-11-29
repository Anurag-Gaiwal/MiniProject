import requests
from bs4 import BeautifulSoup


class ImbFinder:
    def __init__(self):
        self.my_link = "https://www.imdb.com/chart/top/"

    def get_data(self, number):
        ending = int(number)
        respond = requests.get(url=self.my_link)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        data = soup.select(selector=".titleColumn a")
        answer = [tag.string for tag in data]
        return answer[:ending]

