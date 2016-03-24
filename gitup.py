#!/usr/bin/python

import os
from os.path import expanduser
from subprocess import call


class cd:
  """Context manager for changing the current working directory"""
  def __init__(self, newPath):
    self.newPath = expanduser(newPath)

  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)
    print "Entering {} ...\n".format(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)
    print "Entering {} ...\n".format(self.savedPath)


def call_with_message(command, message):
  print message

  return_code = call(command)

  if (return_code == 0):
    print message + " done\n"
  else:
    print message + " failed\n"

  return return_code


def main():
  branch = 'master'

  with cd("~/workspace/source/"):
    call_with_message(["git", "co", branch], "Switching to branch '{}' ...".format(branch))
    call_with_message(["git", "up"], "Pulling and rebasing branch '{}' ...".format(branch))


if __name__ == '__main__':
  main()
