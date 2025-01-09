# pygrocytoo

[![PyPI](https://img.shields.io/pypi/v/pygrocytoo.svg)](https://pypi.org/project/pygrocytoo/)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Grocy Version](https://img.shields.io/badge/grocy-3.1.0-yellow)
[![Coverage Status](https://coveralls.io/repos/github/phunkmaster/pygrocytoo/badge.svg?branch=main)](https://coveralls.io/github/phunkmaster/pygrocytoo?branch=main)
[![CodeFactor](https://www.codefactor.io/repository/github/phunkmaster/pygrocytoo/badge)](https://www.codefactor.io/repository/github/phunkmaster/pygrocytoo)

[//]: # ([![pre-commit]&#40;https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&#41;]&#40;https://github.com/pre-commit/pre-commit&#41;)
[Documentation](https://sebrut.github.io/pygrocy/)

## Installation

`pip install pygrocytoo`

## Usage

Import the package:

```python
from pygrocytoo.grocy import Grocy
```

Obtain a grocy instance:

```python
grocy = Grocy("https://example.com", "GROCY_API_KEY")
```

or

```python
grocy = Grocy("https://example.com", "GROCY_API_KEY", port = 9192, verify_ssl = True)
```

Get current stock:

```python
for entry in grocy.stock():
    print("{} in stock for product id {}".format(entry.available_amount, entry.id))
```

# Support

If you need help using pygrocy check the [discussions](https://github.com/flipper/pygrocy2/issues) section. Feel free to create an issue for feature requests, bugs and errors in the library.

## Development testing

You need tox and Python 3.13 to run the tests. Navigate to the root dir of `pygrocytoo` and execute `tox` to run the tests.
