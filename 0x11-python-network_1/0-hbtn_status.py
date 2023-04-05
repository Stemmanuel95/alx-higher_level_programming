#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status using urllib model."""
import urllib.request


if __name__ == "__main__":
    url_link = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url_link)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8"))))
