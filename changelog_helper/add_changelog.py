#!/usr/bin/env python
from __future__ import unicode_literals

import argparse
import errno
from io import open
import os
import subprocess
import yaml

"""Generate a changelog entry file in git project root.

Automatically stages the file and amends the previous commit if the `--amend` argument is used.
"""


def get_title():
    return subprocess.check_output("git log --format='%s' -1", shell=True).decode('utf-8').strip()


def get_author():
    return subprocess.check_output("git config user.name", shell=True).decode('utf-8').strip()


def get_branch_name():
    return subprocess.check_output("git symbolic-ref --short HEAD", shell=True).decode('utf-8').strip()


def get_git_root():
    return subprocess.check_output("git rev-parse --show-toplevel", shell=True).decode('utf-8').strip()


def get_yml_file_path():
    path = os.path.join(get_git_root(), 'changelogs', 'unreleased')
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    file_name = get_branch_name().replace('/', '-') + '.yml'
    file_path = os.path.join(path, file_name)
    return file_path


def write_changelog(log_entry, force=False):
    file_path = get_yml_file_path()

    if os.path.exists(file_path):
        if force:
            print("File {PATH} already exists, and will be lost.".format(PATH=file_path))
        else:
            print("ERROR: File {PATH} already exists.\nIf you want to rewrite it: use --force flag.".format(PATH=file_path))
            exit(1)

    print("Saving change into file: " + file_path)
    yml_content = yaml.safe_dump(log_entry, allow_unicode=True, default_flow_style=False, encoding=None)
    print(yml_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(yml_content)


def commit_changes(yaml_file_path):
    subprocess.call("git add {FILENAME}".format(FILENAME=yaml_file_path), shell=True)
    subprocess.call("git commit --amend", shell=True)
    print("Changes have been committed to local git repository.")


def main():
    parser = argparse.ArgumentParser(description='Generate a changelog entry file in git project root.')
    parser.add_argument('title', nargs='?', default=get_title())
    parser.add_argument('--author', default=get_author())
    parser.add_argument('--amend', action='store_true')
    parser.add_argument('--force', action='store_true')
    app_args = parser.parse_args()

    log_entry = {
        'title': app_args.title,
        'author': app_args.author
    }

    write_changelog(log_entry, force=app_args.force)
    if app_args.amend:
        commit_changes(get_yml_file_path())


if __name__ == '__main__':
    main()
