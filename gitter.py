#!/usr/bin/env python

# commit git files.

import subprocess


message = raw_input("Enter commit message: ")

print subprocess.call(["git", "add", "-A"])

print subprocess.call(['git', 'commit', '-m', message])
