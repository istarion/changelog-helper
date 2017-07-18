#!/usr/bin/env python
from __future__ import unicode_literals

import argparse
import subprocess

import yaml

# Generate a changelog entry file in git project root.
#
# Automatically stages the file and amends the previous commit if the `--amend`
# argument is used.


def get_title():
    return subprocess.check_output("git log --format='%s' -1", shell=True)


def get_author():
    pass


class ChangelogEntry(object):
    def __init__(self, title=get_title(), author=get_author()):
        self.content = dict()
        self.content['title'] = title
        self.content['author'] = author

    def to_yaml(self):
        return yaml.dump(self.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a changelog entry file in git project root.')
    parser.add_argument('title', nargs='?', default=get_title())
    parser.add_argument('--author', default=get_author())
    app_args = parser.parse_args()

    ChangelogEntry(**app_args.__dict__)
