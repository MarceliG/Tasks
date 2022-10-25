#!/usr/bin/python3
import argparse
import requests
from requests.utils import quote
from bs4 import BeautifulSoup
from typing import Optional, Sequence


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
        translated_words (set): return translated word.
    """
    soup = BeautifulSoup(page.text, "html.parser")
    scrap_meta = str(soup.find_all("meta")[1]).split()
    striped_meta = [x.strip(" ;,'") for x in scrap_meta]
    words = check_direction_translate(striped_meta)

    return words


def check_direction_translate(striped_meta: list):
    """Check direction to translate the word is supposed to be PL>EN or EN>PL

    Args:
        striped_meta (list): <meta> from HTML with translated words and some
        mess

    Returns:
        words_list (list): words in list
    """
    words_list = []
    if "polsku?" in striped_meta:
        # English to Polish
        words_list.append("EN>PL")
    elif "angielsku?" in striped_meta:
        # Polish to English
        words_list.append("PL>EN")
    else:
        print("We don't have this word in our dictionary")

    if len(words_list) == 1:
        for word in striped_meta[16:-1]:
            if word not in words_list:  # I want unique words
                words_list.append(word)
    return words_list


def compare_all_translated_word_to_str(translated_words: list):
    """marge all element from list to string

    Args:
        translated_words (list): list with translated words

    Returns:
        str: string with translated word
    """
    result_as_string = ""
    for word in translated_words:
        result_as_string += word + " "

    return result_as_string


def translate(input_words: list) -> str:
    encoded_word = encoding(input_words)
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
    translate(args.word)
    return 0


if __name__ == "__main__":
    main()
