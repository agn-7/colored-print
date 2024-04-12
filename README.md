Colored Print
-----------------------
[![PyPI](https://img.shields.io/pypi/v/python-colored-print)](https://pypi.org/project/python-colored-print/)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-colored-print)](https://pypi.org/project/python-colored-print/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/agn-7/colored-print/master/LICENSE)

A lightweight python library in order to print in different colors and save them into a file optionally.


## Setup

```bash
pip install python-colored-print
```

## Usage

```python
from colored_print import log

log.success("Hello", 123, "Bye").store()
log.info("Hello", 123, "Bye")
log.warn("Hello", 123, "Bye")
log.err("Hello", 123, "Bye").store(path="log.txt")
log.pink("Hello", 123, "Bye")
log("Hello", 123, "Bye")  # default color is white
log.store("Hello", 123, "Bye")  # only store without printing
```

## Output

![Output](https://i.stack.imgur.com/HMVP6.png)
