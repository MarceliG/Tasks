#!/usr/bin/python3
import argparse
import requests
from requests.utils import quote
from bs4 import BeautifulSoup
from typing import Optional
from typing import Sequence


def encoding(word: str):
    """Encoding any word.

    Args:
        word (str): the word.

    Returns:
        (str): Encoded word.
    """
    try:
        return quote(word, safe="")
    except:
        return ""


def translate(word: str = "") -> str:
    # word = input("słowo do przetłumaczenie:")
    # word = "zamek"
    encoded_word = encoding(word)
    url = "https://www.diki.pl/slownik-angielskiego?q=" + encoded_word
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    elements = str(soup.find_all("meta")[1]).split()
    elements = [x.strip(" '") for x in elements]

    translated = elements[17:-1]
    result = ""
    for i in translated:
        result += i + " "

    print(result)


def main(argument: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description="tranlate any word")
    parser.add_argument("word", help="Enter a word to translate")
    args = parser.parse_args()
    translate(args.word)
    return 0


if __name__ == "__main__":
    main()
