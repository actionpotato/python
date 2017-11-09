#!/usr/bin/env python

#from distutils.spawn import find_executable
#run = find_executable("ls")
#print run

import distutils.spawn

def is_tool(ls):
  return distutils.spawn.find_executable(ls) is not None
print is_tool
