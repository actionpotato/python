#!/usr/bin/env python

# commit git files.
# There is a better way to do this, but I want to practice Understanding
# subprocess

import subprocess


message = raw_input("Enter commit message: ")

print subprocess.call(["git", "add", "-A"])

print subprocess.call(['git', 'commit', '-m', message])
