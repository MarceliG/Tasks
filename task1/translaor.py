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


def send_request(encoded_word: str):
    """Send request to website with word to translate.

    Args:
        encoded_word (str): give encoded word undestandable by HTML

    Returns:
        request : page with HTML
    """
    url = "https://www.diki.pl/slownik-angielskiego?q=" + encoded_word
    return requests.get(url)


def translate(word: str = "") -> str:
    encoded_word = encoding(word)
    page = send_request(encoded_word)
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
