#!/usr/bin/env python

import subprocess


command = subprocess.check_call(["ls","-alh"])

print command

# I did not expect this to be that easy.
