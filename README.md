Installation
============

[![Python package](https://img.shields.io/github/actions/workflow/status/chdemko/pandoc-latex-admonition/python-package.yml?logo=github&branch=develop)](https://github.com/chdemko/pandoc-latex-admonition/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-admonition/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-admonition?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-admonition.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-admonition/)
[![Code Climate](https://img.shields.io/codeclimate/maintainability/chdemko/pandoc-latex-admonition?logo=codeclimate&barnch=develop)](https://codeclimate.com/github/chdemko/pandoc-latex-admonition/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-admonition/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-admonition)
[![Codacy](https://img.shields.io/codacy/grade/443f4a26698a4ba0be5064fe9323f2a0.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-admonition/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-admonition.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-admonition/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-admonition.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-admonition/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-admonition.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-admonition/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-admonition?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-admonition)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-admonition.svg?llogo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-admonition/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-admonition.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-admonition/)
[![Pandoc version](https://img.shields.io/badge/pandoc-3.0%20..%203.6-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-admonition.svg?logo=github)](https://github.com/chdemko/pandoc-latex-admonition/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-admonition/develop?logo=github)](https://github.com/chdemko/pandoc-latex-admonition/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-admonition.svg?logo=github)](http://pandoc-latex-admonition.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-admonition.svg?logo=github)](http://pandoc-latex-admonition.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-admonition.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-admonition)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-admonition.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-admonition.readthedocs.io/en/latest/)

*pandoc-latex-admonition* is a [pandoc] filter for adding admonition
to `div`s or `codeblock`s elements.

It uses the *tcolorbox* LaTeX package to generate admonitions and
the *footnote* LaTeX package to handle correctly footnotes in
admonition.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-admonition* requires [python], a programming language that
comes pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-admonition* using the bash command

~~~shell-session
$ pipx install pandoc-latex-admonition
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-admonition
~~~

`pipx` is a script to install and run python applications in isolated environments from the Python Package Index, [PyPI]. It can be installed using instructions given [here](https://pipx.pypa.io/stable/).

Make sure you have the

* *tcolorbox*
* *footnote*
* *xcolor*
* *ifthen*

LaTeX packages. On linux you have to install some extra libraries **before**
*pandoc-latex-admonition*. On a Debian-based system (including Ubuntu),
you can install it as root using

~~~shell-session
$ sudo apt-get install texlive-latex-extra
~~~

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with pandoc-latex-admonition, please feel
welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-admonition/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

