#!/usr/bin/env python

"""
Pandoc filter for adding admonition in LaTeX
"""

from panflute import *
import uuid

def default_environment():
    return {
        'env': 'env-' + str(uuid.uuid4()),
        'color': 'black',
        'position': 'left',
        'linewidth': 2,
        'margin': -4,
        'innermargin': 5,
        'localfootnotes': False
    }

def x11colors():
    # See https://www.w3.org/TR/css-color-3/#svg-color
    return {
        'aliceblue': 'F0F8FF',
        'antiquewhite': 'FAEBD7',
        'aqua': '00FFFF',
        'aquamarine': '7FFFD4',
        'azure': 'F0FFFF',
        'beige': 'F5F5DC',
        'bisque': 'FFE4C4',
        'black': '000000',
        'blanchedalmond': 'FFEBCD',
        'blue': '0000FF',
        'blueviolet': '8A2BE2',
        'brown': 'A52A2A',
        'burlywood': 'DEB887',
        'cadetblue': '5F9EA0',
        'chartreuse': '7FFF00',
        'chocolate': 'D2691E',
        'coral': 'FF7F50',
        'cornflowerblue': '6495ED',
        'cornsilk': 'FFF8DC',
        'crimson': 'DC143C',
        'cyan': '00FFFF',
        'darkblue': '00008B',
        'darkcyan': '008B8B',
        'darkgoldenrod': 'B8860B',
        'darkgray': 'A9A9A9',
        'darkgreen': '006400',
        'darkgrey': 'A9A9A9',
        'darkkhaki': 'BDB76B',
        'darkmagenta': '8B008B',
        'darkolivegreen': '556B2F',
        'darkorange': 'FF8C00',
        'darkorchid': '9932CC',
        'darkred': '8B0000',
        'darksalmon': 'E9967A',
        'darkseagreen': '8FBC8F',
        'darkslateblue': '483D8B',
        'darkslategray': '2F4F4F',
        'darkslategrey': '2F4F4F',
        'darkturquoise': '00CED1',
        'darkviolet': '9400D3',
        'deeppink': 'FF1493',
        'deepskyblue': '00BFFF',
        'dimgray': '696969',
        'dimgrey': '696969',
        'dodgerblue': '1E90FF',
        'firebrick': 'B22222',
        'floralwhite': 'FFFAF0',
        'forestgreen': '228B22',
        'fuchsia': 'FF00FF',
        'gainsboro': 'DCDCDC',
        'ghostwhite': 'F8F8FF',
        'gold': 'FFD700',
        'goldenrod': 'DAA520',
        'gray': '808080',
        'green': '008000',
        'greenyellow': 'ADFF2F',
        'grey': '808080',
        'honeydew': 'F0FFF0',
        'hotpink': 'FF69B4',
        'indianred': 'CD5C5C',
        'indigo': '4B0082',
        'ivory': 'FFFFF0',
        'khaki': 'F0E68C',
        'lavender': 'E6E6FA',
        'lavenderblush': 'FFF0F5',
        'lawngreen': '7CFC00',
        'lemonchiffon': 'FFFACD',
        'lightblue': 'ADD8E6',
        'lightcoral': 'F08080',
        'lightcyan': 'E0FFFF',
        'lightgoldenrodyellow': 'FAFAD2',
        'lightgray': 'D3D3D3',
        'lightgreen': '90EE90',
        'lightgrey': 'D3D3D3',
        'lightpink': 'FFB6C1',
        'lightsalmon': 'FFA07A',
        'lightseagreen': '20B2AA',
        'lightskyblue': '87CEFA',
        'lightslategray': '778899',
        'lightslategrey': '778899',
        'lightsteelblue': 'B0C4DE',
        'lightyellow': 'FFFFE0',
        'lime': '00FF00',
        'limegreen': '32CD32',
        'linen': 'FAF0E6',
        'magenta': 'FF00FF',
        'maroon': '800000',
        'mediumaquamarine': '66CDAA',
        'mediumblue': '0000CD',
        'mediumorchid': 'BA55D3',
        'mediumpurple': '9370DB',
        'mediumseagreen': '3CB371',
        'mediumslateblue': '7B68EE',
        'mediumspringgreen': '00FA9A',
        'mediumturquoise': '48D1CC',
        'mediumvioletred': 'C71585',
        'midnightblue': '191970',
        'mintcream': 'F5FFFA',
        'mistyrose': 'FFE4E1',
        'moccasin': 'FFE4B5',
        'navajowhite': 'FFDEAD',
        'navy': '000080',
        'oldlace': 'FDF5E6',
        'olive': '808000',
        'olivedrab': '6B8E23',
        'orange': 'FFA500',
        'orangered': 'FF4500',
        'orchid': 'DA70D6',
        'palegoldenrod': 'EEE8AA',
        'palegreen': '98FB98',
        'paleturquoise': 'AFEEEE',
        'palevioletred': 'DB7093',
        'papayawhip': 'FFEFD5',
        'peachpuff': 'FFDAB9',
        'peru': 'CD853F',
        'pink': 'FFC0CB',
        'plum': 'DDA0DD',
        'powderblue': 'B0E0E6',
        'purple': '800080',
        'red': 'FF0000',
        'rosybrown': 'BC8F8F',
        'royalblue': '4169E1',
        'saddlebrown': '8B4513',
        'salmon': 'FA8072',
        'sandybrown': 'F4A460',
        'seagreen': '2E8B57',
        'seashell': 'FFF5EE',
        'sienna': 'A0522D',
        'silver': 'C0C0C0',
        'skyblue': '87CEEB',
        'slateblue': '6A5ACD',
        'slategray': '708090',
        'slategrey': '708090',
        'snow': 'FFFAFA',
        'springgreen': '00FF7F',
        'steelblue': '4682B4',
        'tan': 'D2B48C',
        'teal': '008080',
        'thistle': 'D8BFD8',
        'tomato': 'FF6347',
        'turquoise': '40E0D0',
        'violet': 'EE82EE',
        'wheat': 'F5DEB3',
        'white': 'FFFFFF',
        'whitesmoke': 'F5F5F5',
        'yellow': 'FFFF00',
        'yellowgreen': '9ACD32'
    }

def admonition(elem, doc):
    # Is it in the right format and is it Div or a CodeBlock?
    if doc.format == 'latex' and elem.tag in ['Div', 'CodeBlock']:

        # Is there a latex-admonition-color attribute?
        if 'latex-admonition-color' in elem.attributes:
            environment = define_environment(
                doc,
                elem.attributes,
                'latex-admonition-color',
                'latex-admonition-position',
                'latex-admonition-linewidth',
                'latex-admonition-margin',
                'latex-admonition-innermargin',
                'latex-admonition-localfootnotes'
            )
            doc.added.append(environment)
            return add_latex(elem, environment)
        else:
            # Get the classes
            classes = set(elem.classes)

            # Loop on all fontsize definition
            for environment in doc.defined:

                # Are the classes correct?
                if classes >= environment['classes']:
                    return add_latex(elem,  environment)

def add_latex(elem,  environment):
    images = []
    def extract_images(elem, doc):
        # Extract image which is alone with a title
        if isinstance(elem, Para) and len(elem.content) == 1 and isinstance(elem.content[0], Image) and bool(elem.content[0].content):
            images.append(elem)
            return []
    # The images need to be placed after the framed environment
    return [
        RawBlock('\\begin{' + environment['env'] + '}', 'tex'),
        elem.walk(extract_images),
        RawBlock('\\end{' + environment['env'] + '}', 'tex')
    ] + images

def prepare(doc):
    doc.x11colors = x11colors()

   # Prepare the definitions
    doc.defined = []
    doc.added = []

    # Get the meta data
    meta = doc.get_metadata('pandoc-latex-admonition')

    if isinstance(meta, list):

        # Loop on all definitions
        for definition in meta:

            # Verify the definition
            if isinstance(definition, dict) and 'classes' in definition and isinstance(definition['classes'], list):
                environment = define_environment(doc, definition, 'color', 'position', 'linewidth', 'margin', 'innermargin', 'localfootnotes')
                environment['classes'] = set(definition['classes'])
                doc.defined.append(environment)

def define_environment(doc, definition, key_color, key_position, key_linewidth, key_margin, key_innermargin, key_localfootnotes):
    # Get the default environment
    environment = default_environment()
    define_color(doc, environment, definition, key_color)
    define_position(doc, environment, definition, key_position)
    define_linewidth(doc, environment, definition, key_linewidth)
    define_margin(doc, environment, definition, key_margin)
    define_innermargin(doc, environment, definition, key_innermargin)
    define_localfootnotes(doc, environment, definition, key_localfootnotes)
    return environment

def define_color(doc, environment, definition, key_color):
    # Get the color
    if key_color in definition:
        color = str(definition[key_color]).lower()
        if color in doc.x11colors:
            environment['color'] = color
        else:
            # color must be a valid x11 color (https://www.w3.org/TR/css-color-3/#svg-color)
            debug('[WARNING] pandoc-latex-admonition: ' + color + ' is not a valid x11 color; using ' + environment['color'])

def define_position(doc, environment, definition, key_position):
    # Get the position
    if key_position in definition:
        environment['position'] = str(definition[key_position])

def define_linewidth(doc, environment, definition, key_linewidth):
    # Get the line width
    if key_linewidth in definition:
        try:
            linewidth = int(str(definition[key_linewidth]))
            if linewidth <= 0:
                debug('[WARNING] pandoc-latex-admonition: linewidth must be a positivie integer; using ' + str(environment['linewidth']))
            else:
                environment['linewidth'] = linewidth
        except ValueError:
            debug('[WARNING] pandoc-latex-admonition: linewidth is not a valid; using ' + str(environment['linewidth']))

def define_margin(doc, environment, definition, key_margin):
    # Get the margin
    if key_margin in definition:
        try:
            environment['margin'] = int(str(definition[key_margin]))
        except ValueError:
            debug('[WARNING] pandoc-latex-admonition: margin is not a valid; using ' + str(environment['margin']))

def define_innermargin(doc, environment, definition, key_innermargin):
    # Get the inner margin
    if key_innermargin in definition:
        try:
            environment['innermargin'] = int(str(definition[key_innermargin]))
        except ValueError:
            debug('[WARNING] pandoc-latex-admonition: innermargin is not a valid; using ' + str(environment['innermargin']))

def define_localfootnotes(doc, environment, definition, key_localfootnotes):
    # Get the local footnotes
    if key_localfootnotes in definition:
        environment['localfootnotes'] = str(definition[key_localfootnotes]) == 'true'

def environment_option(position, linewidth, innermargin, margin, color):
    if position == 'right':
       pos = 'right'
       inv = 'left'
    else:
       pos = 'left'
       inv = 'right'

    properties = [
        'topline=false',
        'bottomline=false',
        inv + 'line=false',
        'linewidth=' + str(linewidth) + 'pt',
        'inner' + pos + 'margin=' + str(innermargin) +'pt',
        pos + 'margin=' + str(margin) +'pt',
        'inner' + inv + 'margin=0pt',
        'linecolor=' + color,
        'skipabove=\\topskip'
    ]
    return '[' + ','.join(properties) + ']'

def new_environment(environment):
    if environment['localfootnotes']:
        return '\n'.join([
            '\\newenvironment{' + environment['env'] + '}',
            '{',
            '    \\begin{mdframed}' + environment_option(environment['position'], environment['linewidth'], environment['innermargin'], environment['margin'], environment['color']),
            '}',
            '{',
            '    \\end{mdframed}',
            '}'
        ])
    else:
        return '\n'.join([
            '\\newenvironment{' + environment['env'] + '}',
            '{',
            '    \\savenotes',
            '    \\begin{mdframed}' + environment_option(environment['position'], environment['linewidth'], environment['innermargin'], environment['margin'], environment['color']),
            '    \\let\\thempfootnote=\\thefootnote',
            '    \\let\\oldfootnote\\footnote',
            '    \\renewcommand{\\footnote}[1]{\\stepcounter{footnote}\\oldfootnote{##1}}',
            '}',
            '{',
            '    \\end{mdframed}',
            '    \\spewnotes',
            '}'
        ])

def finalize(doc):
    # Add header-includes if necessary
    if 'header-includes' not in doc.metadata:
        doc.metadata['header-includes'] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata['header-includes'], MetaList):
        doc.metadata['header-includes'] = MetaList(doc.metadata['header-includes'])

    # Add usefull LaTexPackage
    doc.metadata['header-includes'].append(MetaInlines(RawInline('\\usepackage{mdframed}', 'tex')))
    doc.metadata['header-includes'].append(MetaInlines(RawInline('\\usepackage{xcolor}', 'tex')))
    doc.metadata['header-includes'].append(MetaInlines(RawInline('\\usepackage{footnote}', 'tex')))

    # Define x11 colors
    tex = []
    for name, color in doc.x11colors.items():
        tex.append('\\definecolor{' + name.lower() + '}{HTML}{' + color + '}')
    doc.metadata['header-includes'].append(MetaInlines(RawInline('\n'.join(tex), 'tex')))

    # Define specific environments
    for environment in doc.defined + doc.added:
        doc.metadata['header-includes'].append(MetaInlines(RawInline(new_environment(environment), 'tex')))

def main(doc = None):
    return run_filter(admonition, prepare = prepare, finalize = finalize, doc = doc)

if __name__ == '__main__':
    main()

