import requests
import httpx


def main():
    s = httpx.get("https://bab.la/")
    print(s.text)


if __name__ == "__main__":
    main()
