#!/usr/bin/env python
import sys
import getopt
import requests

def usage():
    print("changelog -r <repository_name>")


def get_pull_requests(repository):
    # construct url
    url = "https://api.github.com/repos/" + repository + "/pulls?state=closed?per_page=100" # TODO solve per_page issue

    # request information
    req = requests.get(url)

    # write information to stdout
    pull_requests = req.json()

    return pull_requests


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

    pull_requests = get_pull_requests(repository)

    for pull_request in pull_requests:
        print(pull_request.get("title"))

if __name__ == "__main__":
    main()
