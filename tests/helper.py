# This Python file uses the following encoding: utf-8

from panflute import *

import pandoc_latex_admonition

def conversion(markdown, format='markdown'):
    doc = convert_text(markdown, standalone = True)
    doc.format = format
    pandoc_latex_admonition.main(doc)
    return doc

