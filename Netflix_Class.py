import requests
from bs4 import BeautifulSoup


class NetflixFinder:
    def __init__(self):
        self.my_link = "https://top10.netflix.com/"

    def get_data(self, number):
        ending = int(number)
        respond = requests.get(url=self.my_link)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        data = soup.select(selector="tr td:nth-of-type(2)")
        answer = [tag.getText() for tag in data]
        return answer[:ending]
