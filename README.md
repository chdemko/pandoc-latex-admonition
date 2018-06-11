# pandoc-latex-admonition
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-latex-admonition/1.2.2.svg)](https://travis-ci.org/chdemko/pandoc-latex-admonition/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-admonition/1.2.2.svg)](https://coveralls.io/github/chdemko/pandoc-latex-admonition?branch=1.2.2)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-admonition.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-admonition/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-admonition.svg)](https://pypi.org/project/pandoc-latex-admonition/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-admonition/1.2.2.svg)](https://pypi.org/project/pandoc-latex-admonition/1.2.2/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-admonition/1.2.2.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-admonition/1.2.2/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-admonition.svg)](https://pypi.org/project/pandoc-latex-admonition/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-admonition.svg)](https://pypi.org/project/pandoc-latex-admonition/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-admonition.svg)](https://pypi.org/project/pandoc-latex-admonition/)

*pandoc-latex-admonition* is a [pandoc] filter for adding admonition to `div`s or `codeblock`s elements.

It uses the *mdframed* LaTeX package to generate admonitions and the *footnote* LaTeX package to handle correctly footnotes in admonition.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-admonition/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-admonition

Installation
------------

*pandoc-latex-admonition* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-admonition* as root using the bash command

    pip install pandoc-latex-admonition

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-admonition

To upgrade to the current code, use

    pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-admonition

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

Make sure you have the *mdframed* LaTeX package. On linux you have to install some extra libraries **before** *pandoc-latex-admonition*. On a Debian-based system (including Ubuntu), you can install it as root using

	apt-get texlive-latex-extra

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with pandoc-latex-admonition, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-admonition/issues

