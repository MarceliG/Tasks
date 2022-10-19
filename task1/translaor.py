#!/usr/bin/python3
import argparse
from operator import index
import requests
from requests.utils import quote
from bs4 import BeautifulSoup
from typing import Optional
from typing import Sequence


def encoding(words: list):
    """Encoding any word.

    Args:
        word (list): the word.

    Returns:
        (str): Encoded word/words.
    """

    try:
        result = ""
        for word in words:
            result += quote(word, safe="")
            if words.index(word) < len(words) and words.index(word) > 0:
                result += "+"
        print(result)
        return result
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


def give_only_tranlated_words(page):
    """Extract translated world.

    Args:
        page: HTML from request

    Returns:
        translated_words (list): return translated word.
    """
    soup = BeautifulSoup(page.text, "html.parser")
    elements = str(soup.find_all("meta")[1]).split()
    elements = [x.strip(" '") for x in elements]
    return elements[17:-1]


def compare_all_translated_word_to_str(translated_words: list):
    """marge all element from list to string

    Args:
        translated_words (list): list with translated words

    Returns:
        str: string with translated word
    """
    result_as_string = ""
    for i in translated_words:
        result_as_string += i + " "
    return result_as_string


def translate(word: list) -> str:
    encoded_word = encoding(word)
    page = send_request(encoded_word)
    translated_words = give_only_tranlated_words(page)
    result = compare_all_translated_word_to_str(translated_words)

    print(result)


def main(argument: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description="tranlate any word")
    parser.add_argument(
        "word", type=str, nargs="+", help="Enter a word to translate"
    )
    args = parser.parse_args()
    print(args.word)
    translate(args.word)
    return 0


if __name__ == "__main__":
    main()
