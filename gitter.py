#!/usr/bin/env python

# commit git files.

import subprocess


message = raw_input("Enter commit message: ")

print subprocess.check_call(["git", "add", "-A"])

print subprocess.check_call(['git', 'commit', '-m', message])
