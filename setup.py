"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/chdemko/pandoc-latex-admonition
"""

# To use a consistent encoding
import codecs
import os

# Always prefer setuptools over distutils
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert("README.md", "rst")
except (IOError, ImportError):
    with codecs.open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = f.read()


setup(
    name="pandoc-latex-admonition",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="1.3.1",
    # The project's description
    description="A pandoc filter for adding admonition in LaTeX",
    long_description=LONG_DESCRIPTION,
    # The project's main homepage.
    url="https://github.com/chdemko/pandoc-latex-admonition",
    # The project's download page
    download_url="https://github.com/chdemko/pandoc-latex-admonition/archive/master.zip",
    # Author details
    author="Christophe Demko",
    author_email="chdemko@gmail.com",
    # Maintainer details
    maintainer="Christophe Demko",
    maintainer_email="chdemko@gmail.com",
    # Choose your license
    license="BSD-3-Clause",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        # Specify the OS
        "Operating System :: OS Independent",
        # Indicate who your project is intended for
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
    ],
    # What does your project relate to?
    keywords="pandoc filters latex admonition",
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["pandoc_latex_admonition"],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": ["pandoc-latex-admonition = pandoc_latex_admonition:main"]
    },
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["panflute>=1.10", "pypandoc>=1.4"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={"dev": ["check-manifest"], "test": ["coverage"]},
    # packages=find_packages(),
    # include_package_data = True,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "coverage"],
)
