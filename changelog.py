#!/usr/bin/env python

import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "hr:")

repository = ""

for option, value in opts:
    if option == "-r":
        repository = value


url = "https://api.github.com/repos/" + repository + "/pulls"

print(url)
