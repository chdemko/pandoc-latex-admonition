#!/usr/bin/env python

"""
Pandoc filter for adding admonition in LaTeX
"""

from pandocfilters import RawBlock, Para, stringify, toJSONFilters, walk
from functools import reduce

import io
import sys
import codecs
import json
import uuid

defined = []

def admonition(key, value, format, meta):
    global defined

    # Is it a div and the right format?
    if key == 'Div' and format == 'latex':

        # Get the attributes
        [[id, classes, properties], content] = value

        currentClasses = set(classes)
        for elt in getDefined(meta):

            # Is the classes correct?
            if currentClasses >= elt['classes']:
                [images, content] = getImages(content)
                value[1] = [RawBlock('tex', '\\begin{' + elt['env'] + '}')] + content + [RawBlock('tex', '\\end{' + elt['env'] + '}')]

                # The images need to be placed after the framed environment
                if images:
                    value[1].extend(images)
                break

def defaultEnvironment(color, classes):
    return {
        'classes': set(classes),
        'env': 'env-' + str(uuid.uuid4()),
        'color': color,
        'position': 'left',
        'linewidth': 2,
        'margin': -4,
        'innermargin': 5,
    }

def getDefined(meta):
    if not hasattr(getDefined, 'value'):

        getDefined.value = []
        if 'pandoc-latex-admonition' in meta and meta['pandoc-latex-admonition']['t'] == 'MetaList':
            for definition in meta['pandoc-latex-admonition']['c']:
                if definition['t'] == 'MetaMap':
                    if 'classes' in definition['c'] and definition['c']['classes']['t'] == 'MetaList':
                        if 'color' in definition['c']:
                            color = stringify(definition['c']['color'])
                        else:
                            color = 'Black'
                        # color must be a valid LaTeX color (https://en.wikibooks.org/wiki/LaTeX/Colors)
                        adm = {
                            'env': 'env-' + str(uuid.uuid4()),
                            'color': color,
                            'position': 'left',
                            'linewidth': 2,
                            'margin': -4,
                            'innermargin': 5
                        }
                        classes = []
                        for klass in definition['c']['classes']['c']:
                            classes.append(stringify(klass))
                        adm['classes'] = set(classes)
                        if 'position' in definition['c']:
                            adm['position'] = stringify(definition['c']['position'])
                        if 'linewidth' in definition['c'] and definition['c']['linewidth']['t'] == 'MetaString':
                            try:
                                adm['linewidth'] = int(definition['c']['linewidth']['c'])
                            except ValueError:
                                pass
                        if 'margin' in definition['c'] and definition['c']['margin']['t'] == 'MetaString':
                            try:
                                adm['margin'] = int(definition['c']['margin']['c'])
                            except ValueError:
                                pass
                        if 'innermargin' in definition['c'] and definition['c']['innermargin']['t'] == 'MetaString':
                            try:
                                adm['innermargin'] = int(definition['c']['innermargin']['c'])
                            except ValueError:
                                pass
                        getDefined.value.append(adm)
        if 'header-includes' not in meta:
            meta['header-includes'] = {u'c': [], u't': u'MetaList'}
        meta['header-includes']['c'].append({
            'c': [{'t': 'RawInline', 'c': ['tex', '\\usepackage{mdframed}']}],
            't': 'MetaInlines'
        })
        meta['header-includes']['c'].append({
            'c': [{'t': 'RawInline', 'c': ['tex', '\\usepackage{xcolor}']}],
            't': 'MetaInlines'
        })
        
        x11colors = {
            'AliceBlue': 'F0F8FF',
            'AntiqueWhite': 'FAEBD7',
            'Aqua': '00FFFF',
            'Aquamarine': '7FFFD4',
            'Azure': 'F0FFFF',
            'Beige': 'F5F5DC',
            'Bisque': 'FFE4C4',
            'Black': '000000',
            'BlanchedAlmond': 'FFEBCD',
            'Blue': '0000FF',
            'BlueViolet': '8A2BE2',
            'Brown': 'A52A2A',
            'BurlyWood': 'DEB887',
            'CadetBlue': '5F9EA0',
            'Chartreuse': '7FFF00',
            'Chocolate': 'D2691E',
            'Coral': 'FF7F50',
            'CornflowerBlue': '6495ED',
            'Cornsilk': 'FFF8DC',
            'Crimson': 'DC143C',
            'Cyan': '00FFFF',
            'DarkBlue': '00008B',
            'DarkCyan': '008B8B',
            'DarkGoldenrod': 'B8860B',
            'DarkGray': 'A9A9A9',
            'DarkGreen': '006400',
            'DarkKhaki': 'BDB76B',
            'DarkMagenta': '8B008B',
            'DarkOliveGreen': '556B2F',
            'DarkOrange': 'FF8C00',
            'DarkOrchid': '9932CC',
            'DarkRed': '8B0000',
            'DarkSalmon': 'E9967A',
            'DarkSeaGreen': '8FBC8F',
            'DarkSlateBlue': '483D8B',
            'DarkSlateGray': '2F4F4F',
            'DarkTurquoise': '00CED1',
            'DarkViolet': '9400D3',
            'DeepPink': 'FF1493',
            'DeepSkyBlue': '00BFFF',
            'DimGray': '696969',
            'DodgerBlue': '1E90FF',
            'FireBrick': 'B22222',
            'FloralWhite': 'FFFAF0',
            'ForestGreen': '228B22',
            'Fuchsia': 'FF00FF',
            'Gainsboro': 'DCDCDC',
            'GhostWhite': 'F8F8FF',
            'Gold': 'FFD700',
            'Goldenrod': 'DAA520',
            'Gray': '808080',
            'Green': '008000',
            'GreenYellow': 'ADFF2F',
            'Honeydew': 'F0FFF0',
            'HotPink': 'FF69B4',
            'IndianRed': 'CD5C5C',
            'Indigo': '4B0082',
            'Ivory': 'FFFFF0',
            'Khaki': 'F0E68C',
            'Lavender': 'E6E6FA',
            'LavenderBlush': 'FFF0F5',
            'LawnGreen': '7CFC00',
            'LemonChiffon': 'FFFACD',
            'LightBlue': 'ADD8E6',
            'LightCoral': 'F08080',
            'LightCyan': 'E0FFFF',
            'LightGoldenrodYellow': 'FAFAD2',
            'LightGreen': '90EE90',
            'LightGrey': 'D3D3D3',
            'LightPink': 'FFB6C1',
            'LightSalmon': 'FFA07A',
            'LightSeaGreen': '20B2AA',
            'LightSkyBlue': '87CEFA',
            'LightSlateGray': '778899',
            'LightSteelBlue': 'B0C4DE',
            'LightYellow': 'FFFFE0',
            'Lime': '00FF00',
            'LimeGreen': '32CD32',
            'Linen': 'FAF0E6',
            'Magenta': 'FF00FF',
            'Maroon': '800000',
            'MediumAquamarine': '66CDAA',
            'MediumBlue': '0000CD',
            'MediumOrchid': 'BA55D3',
            'MediumPurple': '9370DB',
            'MediumSeaGreen': '3CB371',
            'MediumSlateBlue': '7B68EE',
            'MediumSpringGreen': '00FA9A',
            'MediumTurquoise': '48D1CC',
            'MediumVioletRed': 'C71585',
            'MidnightBlue': '191970',
            'MintCream': 'F5FFFA',
            'MistyRose': 'FFE4E1',
            'Moccasin': 'FFE4B5',
            'NavajoWhite': 'FFDEAD',
            'Navy': '000080',
            'OldLace': 'FDF5E6',
            'Olive': '808000',
            'OliveDrab': '6B8E23',
            'Orange': 'FFA500',
            'OrangeRed': 'FF4500',
            'Orchid': 'DA70D6',
            'PaleGoldenrod': 'EEE8AA',
            'PaleGreen': '98FB98',
            'PaleTurquoise': 'AFEEEE',
            'PaleVioletRed': 'DB7093',
            'PapayaWhip': 'FFEFD5',
            'PeachPuff': 'FFDAB9',
            'Peru': 'CD853F',
            'Pink': 'FFC0CB',
            'Plum': 'DDA0DD',
            'PowderBlue': 'B0E0E6',
            'Purple': '800080',
            'Red': 'FF0000',
            'RosyBrown': 'BC8F8F',
            'RoyalBlue': '4169E1',
            'SaddleBrown': '8B4513',
            'Salmon': 'FA8072',
            'SandyBrown': 'F4A460',
            'SeaGreen': '2E8B57',
            'Seashell': 'FFF5EE',
            'Sienna': 'A0522D',
            'Silver': 'C0C0C0',
            'SkyBlue': '87CEEB',
            'SlateBlue': '6A5ACD',
            'SlateGray': '708090',
            'Snow': 'FFFAFA',
            'SpringGreen': '00FF7F',
            'SteelBlue': '4682B4',
            'Tan': 'D2B48C',
            'Teal': '008080',
            'Thistle': 'D8BFD8',
            'Tomato': 'FF6347',
            'Turquoise': '40E0D0',
            'Violet': 'EE82EE',
            'Wheat': 'F5DEB3',
            'White': 'FFFFFF',
            'WhiteSmoke': 'F5F5F5',
            'Yellow': 'FFFF00',
            'YellowGreen': '9ACD32'
        }

        tex = []
        for name in x11colors:
            tex.append('\\definecolor{' + name + '}{HTML}{' + x11colors[name] + '}')

        meta['header-includes']['c'].append({
            'c': [{'t': 'RawInline', 'c': ['tex', '\n'.join(tex)]}],
            't': 'MetaInlines'
        })

        for elt in getDefined.value:
            if elt['position'] == 'right':
               pos = 'right'
               inv = 'left'
            else:
               pos = 'left'
               inv = 'right'
            properties = []
            properties.append('topline=false')
            properties.append('bottomline=false')
            properties.append(inv + 'line=false')
            properties.append('linewidth=' + str(elt['linewidth']) + 'pt')
            properties.append('inner' + pos + 'margin=' + str(elt['innermargin']) +'pt')
            properties.append(pos + 'margin=' + str(elt['margin']) +'pt')
            properties.append('inner' + inv + 'margin=0pt')
            properties.append('linecolor=' + elt['color'])
            properties.append('skipabove=\\topskip')
            
            meta['header-includes']['c'].append({
                'c': [{'t': 'RawInline', 'c': ['tex', '\\newmdenv[' + ','.join(properties) + ']{' + elt['env'] + '}']}] ,
                't': 'MetaInlines'
            })
    return getDefined.value

def getImages(x):
    if isinstance(x, list):
        images = []
        content = []
        for item in x:
            [itemImages, itemContent] = getImages(item)
            images = images + itemImages
            if itemContent != None:
                content.append(itemContent)
        return [images, content]
    elif isinstance(x, dict):
        if 't' in x:
            if x['t'] == 'Para' and len(x['c']) == 1 and x['c'][0]['t'] == 'Image':
                return [[x], None]
            else:
                [images, content] = getImages(x['c'] if 'c' in x else None)
                return [images, {'t': x['t'], 'c': content}]
        else:
            return [[], x]
    else:
        return [[], x]

def main():
    toJSONFilters([admonition])

if __name__ == '__main__':
    main()

