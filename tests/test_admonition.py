# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_admonition

from helper import conversion

def test_codeblock_classes():
    doc = conversion(
        '''
---
pandoc-latex-admonition:
  - classes: ['class1', 'class2']
    color: red
    position: right
    linewidth: 5
    innermargin: -8
    margin: 10
---
~~~{.class1 .class2}
~~~
        ''',
        'latex'
    )
    text = convert_text(doc, input_format='panflute', output_format='latex', extra_args=['--wrap=none'])
    assert '\\begin{env-' in text
    assert '\\end{env-' in text
    assert pandoc_latex_admonition.environment_option('right', 5, -8, 10, 'red') in doc.get_metadata()['header-includes'][-1]

def test_codeblock_attributes():
    doc = conversion(
        '''
::: {latex-admonition-color=xyz latex-admonition-linewidth=xyz' latex-admonition-margin=xyz latex-admonition-innermargin=xyz latex-admonition-localfootnotes=true} :::
:::::::::
        ''',
        'latex'
    )
    text = convert_text(doc, input_format='panflute', output_format='latex', extra_args=['--wrap=none'])
    assert '\\begin{env-' in text
    assert '\\end{env-' in text
    assert pandoc_latex_admonition.environment_option('left', 2, 5, -4, 'black') in doc.get_metadata()['header-includes'][-1]

def test_codeblock_images():
    doc = conversion(
        '''
::: {latex-admonition-color=black} :::

![Title]()

Hello
:::::::::
        ''',
        'latex'
    )
    text = convert_text(doc, input_format='panflute', output_format='latex', extra_args=['--wrap=none'])
    assert '\\begin{env-' in text
    assert '\\end{env-' in text
    assert pandoc_latex_admonition.environment_option('left', 2, 5, -4, 'black') in doc.get_metadata()['header-includes'][-1]
    assert isinstance(doc.content[-1], Para)
    assert isinstance(doc.content[-1].content[0], Image)

