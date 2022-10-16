import requests
from bs4 import BeautifulSoup


def main():
    word = "jab%C5%82ko"
    url = "https://www.diki.pl/slownik-angielskiego?q=" + word

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    elements = soup.find_all("meta")
    translated_word = str(elements[1])
    print(translated_word.split(" ")[-2])


if __name__ == "__main__":
    main()
