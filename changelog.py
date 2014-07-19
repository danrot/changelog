#!/usr/bin/env python

import sys
import getopt
import requests

# read arguments
opts, args = getopt.getopt(sys.argv[1:], "hr:")

repository = ""

for option, value in opts:
    if option == "-r":
        repository = value

# construct url
url = "https://api.github.com/repos/" + repository + "/pulls"

# request information
req = requests.get(url)

# write information to stdout
for pull_request in req.json():
    print(pull_request.get("title"))
