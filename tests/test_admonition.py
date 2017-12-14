# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_admonition

def test_codeblock_classes():
    elem = CodeBlock('', classes=['class1', 'class2'])
    metadata = {
        'pandoc-latex-admonition': MetaList(
            MetaMap(
                classes=MetaList(MetaString('class1'), MetaString('class2')),
                color=MetaString('red'),
                position=MetaString('right'),
                linewidth=MetaString('5'),
                innermargin=MetaString('-8'),
                margin=MetaString('10')
            )
        )
    }
    doc = Doc(elem, metadata=metadata, format='latex', api_version=(1, 17, 2))
    pandoc_latex_admonition.main(doc)
    assert doc.content[0].format == 'tex'
    assert doc.content[2].format == 'tex'
    assert pandoc_latex_admonition.environment_option('right', 5, -8, 10, 'red') in doc.get_metadata()['header-includes'][-1]

def test_codeblock_attributes():
    elem = Div(
        attributes={
            'latex-admonition-color': 'xyz',
            'latex-admonition-linewidth': 'xyz',
            'latex-admonition-margin': 'xyz',
            'latex-admonition-innermargin': 'xyz',
            'latex-admonition-localfootnotes': 'true'
        }
    )
    doc = Doc(elem, format='latex', api_version=(1, 17, 2))
    pandoc_latex_admonition.main(doc)
    assert doc.content[0].format == 'tex'
    assert doc.content[2].format == 'tex'
    assert pandoc_latex_admonition.environment_option('left', 2, 5, -4, 'black') in doc.get_metadata()['header-includes'][-1]

def test_codeblock_images():
    elem = Div(
        Para(Image(Str('Title'))),
        Para(Str('Hello')),
        
        attributes={
            'latex-admonition-color': 'black',
        },
    )
    doc = Doc(elem, format='latex', api_version=(1, 17, 2))
    pandoc_latex_admonition.main(doc)
    assert isinstance(doc.content[-1], Para)
    assert isinstance(doc.content[-1].content[0], Image)

