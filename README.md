# changelog_helper

These Python2/3 compatible scripts can create and compile changelog files from different `git` 
branches without conflicts.

Inspired by GitLab team approach to changelogs.
<https://docs.gitlab.com/ee/development/changelog.html>

## How to install:
`pip install changelog_helper`

## Info

Adding changelog entities:

    add_changelog.py [-h] [--author AUTHOR] [--amend] [--force] [title]
    
    Generate a changelog entry file in git project root.
    
    positional arguments:
      title
    
    optional arguments:
      -h, --help       show this help message and exit
      --author AUTHOR
      --amend
      --force

Release version and compile changelog:

    release_changelog.py [-h] [--rebuild] [version]
    
    Generate CHANGELOG.md file from changelog yml files.
    
    positional arguments:
      version     New version, in format like v5.6.7
    
    optional arguments:
      -h, --help  show this help message and exit
      --rebuild

You can move your old changelog to `changelogs/archive.md`, and it will be appended to CHANGELOG.md 
