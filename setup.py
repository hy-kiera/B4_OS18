from os.path import abspath, dirname, join
from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = 'redlist',
    version = '0.0.2',
    description = 'A simple schedule managing cli app',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/Ramenseller/RedList',
    download_url     = 'https://github.com/Ramenseller/RedList/archive/master.tar.gz',
    author = 'Hayeong Lee',
    author_email = 'bb.kiera@gmail.com',
    license = 'MIT LICENSE',
    classifiers = [
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords = ['todo list', 'todo cli', 'task manager'],
    packages = find_packages(exclude=[]),
    install_requires = ['inquirer', 'prettytable'],
    entry_points = {
        'console_scripts': [
            'RedList=redlist.main:main',
        ]
    }
)
