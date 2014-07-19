#!/usr/bin/env python
import sys
import getopt
import requests

def usage():
    print("changelog -r <repository_name> -f <tag>")


def get_pull_requests(repository):
    # request information
    req_pull_requests = requests.get("https://api.github.com/repos/" + repository + "/pulls?state=closed")

    # write information to stdout
    pull_requests = req_pull_requests.json()

    return pull_requests

def get_date_by_tag(repository, tag_name):
    req_tags = requests.get("https://api.github.com/repos/" + repository + "/tags")

    date = None

    for tag in req_tags.json():
        if tag.get("name") == tag_name:
            req_commit = requests.get(tag.get("commit").get("url"))
            date = req_commit.json().get("commit").get("author").get("date")

    return date

def main():
    # read arguments
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:f:")
    except getopt.GetoptError as err:
        print(err)
        usage()

    repository = None
    from_tag = None

    for option, value in opts:
        if option == "-r":
            repository = value
        if option == "-f":
            from_tag = value

    from_date = get_date_by_tag(repository, from_tag)
    print(from_date)

    pull_requests = get_pull_requests(repository)

    for pull_request in pull_requests:
        print(pull_request.get("title"))

if __name__ == "__main__":
    main()
