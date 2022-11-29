import requests
from bs4 import BeautifulSoup

ADDRESS = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


class EmpireFinder:
    def __init__(self):
        self.api_link = ADDRESS

    def get_data(self, number):
        ending = int(number)
        respond = requests.get(url=self.api_link)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        data = soup.find_all(name="h3", class_="title")
        answer = [tag.getText().split(")")[-1].strip() for tag in data]
        return answer[:ending]
