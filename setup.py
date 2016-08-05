import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('cfat/cfat.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cfat",
    packages = ["cfat"],
    entry_points = {
        "console_scripts": ['cfat = cfat.cfat:main']
        },
    version = version,
    description = "A simple tool to help you save time during a codeforces contest.",
    long_description = long_descr,
    author = "Rohith R",
    author_email = "rohithr31@gmail.com",
    url = "https://github.com/MadaraUchiha-314/codeforces-auto-tester",
    install_requires=[
          'bs4',
      ],
    )