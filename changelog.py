#!/usr/bin/env python
import sys
import getopt
import requests

def usage():
    print("changelog -r <repository_name>")


def build_url(repository):
    url = "https://api.github.com/repos/" + repository + "/pulls?state=closed"
    return url


def main():
    # read arguments
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:")
    except getopt.GetoptError as err:
        print(err)
        usage()

    repository = ""

    for option, value in opts:
        if option == "-r":
            repository = value

    # construct url
    url = build_url(repository)

    # request information
    req = requests.get(url)

    # write information to stdout
    for pull_request in req.json():
        print(pull_request.get("title"))

if __name__ == "__main__":
    main()
