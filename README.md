# SkibidibidiPy
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python application](https://github.com/YannLeBezvoet/SkibidibidiPy/actions/workflows/python-app.yml/badge.svg)](https://github.com/YannLeBezvoet/SkibidibidiPy/actions/workflows/python-app.yml)
## Presentation
SkibidibidiPy preprocesses a code written in SkibidibidiPython to transform it into Python
## Installation
Clone the repo, install virtual env for skibidibidiPy whit pipenv.
```
git clone git@github.com:YannLeBezvoet/SkibidibidiPy.git
pipenv install
```
If pipenv is not installed, please refer to pipenv documentation [Pipenv Installation]("https://github.com/pypa/pipenv?tab=readme-ov-file#installation")
## Usage
Run the following command:
```
pipenv run main path/to/template path/to/code
```
The result in Python is in the .out folder
