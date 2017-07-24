import os
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist
from wheel.bdist_wheel import bdist_wheel
from changelog_helper.version import __version__ as app_version


def info(message):
    print('\033[92m{0}\033[0m'.format(message))


def error(message):
    print('\033[91m{0}\033[0m'.format(message))


class DistWheel(bdist_wheel):
    def run(self):
        bdist_wheel.run(self)
        info('-' * 100)
        info('-----Build wheel DONE')
        info('-' * 100)


class Sdist(sdist):
    def run(self):
        sdist.run(self)
        info('-' * 100)
        info('-----Build sdist DONE')
        info('-' * 100)


here = os.path.abspath(os.path.dirname(__file__))

try:
    LONG_DESCRIPTION = open(os.path.join(here, "README.rst")).read()
except IOError:
    LONG_DESCRIPTION = ""

with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.read()
setup(
    name='changelog-helper',
    version=app_version,
    description='Simple scripts for creating and compiling changelog files.',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Environment :: Console"
    ],
    author='Sergey Zavgorodniy',
    author_email='s.zavgorodniy@i-dgtl.ru',
    url='https://github.com/istarion/changelog-helper',
    download_url='https://github.com/istarion/changelog-helper/archive/{VERSION}.tar.gz'.format(VERSION=app_version),
    keywords='git changelog generator',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'add-changelog = changelog_helper.add_changelog:main',
            'release-changelog = changelog_helper.release_changelog:main'
        ]
    },
    cmdclass={
        'bdist_wheel': DistWheel,
        'sdist': Sdist
    }
)
