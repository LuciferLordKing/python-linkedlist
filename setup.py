import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'python-linkedlist',
    version = '21.1.1',
    scripts = ['linkedadt.py'],
    author = "Lucifer Fung",
    author_email = "luciferfung210@gmail.com",
    description = "Linkedlist in Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/LuciferLordKing/python-linkedlist",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        ],
 )
