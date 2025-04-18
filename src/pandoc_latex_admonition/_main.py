#!/usr/bin/env python

"""
Pandoc filter for adding admonition in LaTeX.
"""

import uuid
from typing import Any

from panflute import (
    Doc,
    Element,
    Figure,
    MetaBool,
    MetaInlines,
    MetaList,
    Note,
    RawBlock,
    RawInline,
    convert_text,
    debug,
    run_filter,
)


def default_environment() -> dict[str, Any]:
    """
    Get the default environment.

    Returns
    -------
    dict[str, Any]
        The default environment
    """
    return {
        "env": "env-" + str(uuid.uuid4()),
        "color": "black",
        "position": "left",
        "linewidth": 2,
        "margin": -4,
        "innermargin": 5,
        "localfootnotes": False,
        "nobreak": False,
    }


def x11colors() -> dict[str, str]:
    """
    Get the x11 colors.

    Returns
    -------
    dict[str, str]
        The x11 colors
    """
    # See https://www.w3.org/TR/css-color-3/#svg-color
    return {
        "aliceblue": "F0F8FF",
        "antiquewhite": "FAEBD7",
        "aqua": "00FFFF",
        "aquamarine": "7FFFD4",
        "azure": "F0FFFF",
        "beige": "F5F5DC",
        "bisque": "FFE4C4",
        "black": "000000",
        "blanchedalmond": "FFEBCD",
        "blue": "0000FF",
        "blueviolet": "8A2BE2",
        "brown": "A52A2A",
        "burlywood": "DEB887",
        "cadetblue": "5F9EA0",
        "chartreuse": "7FFF00",
        "chocolate": "D2691E",
        "coral": "FF7F50",
        "cornflowerblue": "6495ED",
        "cornsilk": "FFF8DC",
        "crimson": "DC143C",
        "cyan": "00FFFF",
        "darkblue": "00008B",
        "darkcyan": "008B8B",
        "darkgoldenrod": "B8860B",
        "darkgray": "A9A9A9",
        "darkgreen": "006400",
        "darkgrey": "A9A9A9",
        "darkkhaki": "BDB76B",
        "darkmagenta": "8B008B",
        "darkolivegreen": "556B2F",
        "darkorange": "FF8C00",
        "darkorchid": "9932CC",
        "darkred": "8B0000",
        "darksalmon": "E9967A",
        "darkseagreen": "8FBC8F",
        "darkslateblue": "483D8B",
        "darkslategray": "2F4F4F",
        "darkslategrey": "2F4F4F",
        "darkturquoise": "00CED1",
        "darkviolet": "9400D3",
        "deeppink": "FF1493",
        "deepskyblue": "00BFFF",
        "dimgray": "696969",
        "dimgrey": "696969",
        "dodgerblue": "1E90FF",
        "firebrick": "B22222",
        "floralwhite": "FFFAF0",
        "forestgreen": "228B22",
        "fuchsia": "FF00FF",
        "gainsboro": "DCDCDC",
        "ghostwhite": "F8F8FF",
        "gold": "FFD700",
        "goldenrod": "DAA520",
        "gray": "808080",
        "green": "008000",
        "greenyellow": "ADFF2F",
        "grey": "808080",
        "honeydew": "F0FFF0",
        "hotpink": "FF69B4",
        "indianred": "CD5C5C",
        "indigo": "4B0082",
        "ivory": "FFFFF0",
        "khaki": "F0E68C",
        "lavender": "E6E6FA",
        "lavenderblush": "FFF0F5",
        "lawngreen": "7CFC00",
        "lemonchiffon": "FFFACD",
        "lightblue": "ADD8E6",
        "lightcoral": "F08080",
        "lightcyan": "E0FFFF",
        "lightgoldenrodyellow": "FAFAD2",
        "lightgray": "D3D3D3",
        "lightgreen": "90EE90",
        "lightgrey": "D3D3D3",
        "lightpink": "FFB6C1",
        "lightsalmon": "FFA07A",
        "lightseagreen": "20B2AA",
        "lightskyblue": "87CEFA",
        "lightslategray": "778899",
        "lightslategrey": "778899",
        "lightsteelblue": "B0C4DE",
        "lightyellow": "FFFFE0",
        "lime": "00FF00",
        "limegreen": "32CD32",
        "linen": "FAF0E6",
        "magenta": "FF00FF",
        "maroon": "800000",
        "mediumaquamarine": "66CDAA",
        "mediumblue": "0000CD",
        "mediumorchid": "BA55D3",
        "mediumpurple": "9370DB",
        "mediumseagreen": "3CB371",
        "mediumslateblue": "7B68EE",
        "mediumspringgreen": "00FA9A",
        "mediumturquoise": "48D1CC",
        "mediumvioletred": "C71585",
        "midnightblue": "191970",
        "mintcream": "F5FFFA",
        "mistyrose": "FFE4E1",
        "moccasin": "FFE4B5",
        "navajowhite": "FFDEAD",
        "navy": "000080",
        "oldlace": "FDF5E6",
        "olive": "808000",
        "olivedrab": "6B8E23",
        "orange": "FFA500",
        "orangered": "FF4500",
        "orchid": "DA70D6",
        "palegoldenrod": "EEE8AA",
        "palegreen": "98FB98",
        "paleturquoise": "AFEEEE",
        "palevioletred": "DB7093",
        "papayawhip": "FFEFD5",
        "peachpuff": "FFDAB9",
        "peru": "CD853F",
        "pink": "FFC0CB",
        "plum": "DDA0DD",
        "powderblue": "B0E0E6",
        "purple": "800080",
        "red": "FF0000",
        "rosybrown": "BC8F8F",
        "royalblue": "4169E1",
        "saddlebrown": "8B4513",
        "salmon": "FA8072",
        "sandybrown": "F4A460",
        "seagreen": "2E8B57",
        "seashell": "FFF5EE",
        "sienna": "A0522D",
        "silver": "C0C0C0",
        "skyblue": "87CEEB",
        "slateblue": "6A5ACD",
        "slategray": "708090",
        "slategrey": "708090",
        "snow": "FFFAFA",
        "springgreen": "00FF7F",
        "steelblue": "4682B4",
        "tan": "D2B48C",
        "teal": "008080",
        "thistle": "D8BFD8",
        "tomato": "FF6347",
        "turquoise": "40E0D0",
        "violet": "EE82EE",
        "wheat": "F5DEB3",
        "white": "FFFFFF",
        "whitesmoke": "F5F5F5",
        "yellow": "FFFF00",
        "yellowgreen": "9ACD32",
    }


# pylint: disable=inconsistent-return-statements
def admonition(elem: Element, doc: Doc) -> Element | None:
    """
    Add admonition to elem.

    Arguments
    ---------
    elem
        The current element
    doc
        The pandoc document

    Returns
    -------
    Element | None
        The modified element or None
    """
    # Is it in the right format and is it Div or a CodeBlock?
    if doc.format in ("latex", "beamer") and elem.tag in ("Div", "CodeBlock"):
        # Is there a latex-admonition-color attribute?
        if "latex-admonition-color" in elem.attributes:
            environment = define_environment(
                doc,
                elem.attributes,
                "latex-admonition-color",
                "latex-admonition-position",
                "latex-admonition-linewidth",
                "latex-admonition-margin",
                "latex-admonition-innermargin",
                "latex-admonition-localfootnotes",
                "latex-admonition-nobreak",
            )
            doc.added.append(environment)
            return add_latex(elem, environment)
        # Get the classes
        classes = set(elem.classes)

        # Loop on all font size definition
        for environment in doc.defined:
            # Are the classes correct?
            if any(classes >= defined for defined in environment["classes"]):
                return add_latex(elem, environment)
    return None


def add_latex(elem: Element, environment: dict[str, Any]) -> Element | None:
    """
    Add LaTeX code to the element.

    Arguments
    ---------
    elem
        The current element

    environment
        The environment to add

    Returns
    -------
    Element | None
        The modified element
    """

    def note(element, doc):
        if (
            isinstance(element, Note)
            and doc.format == "beamer"
            and not environment["localfootnotes"]
        ):
            return RawInline(
                "".join(
                    [
                        "\\footnote<.->[frame]{",
                        convert_text(
                            element.content,
                            input_format="panflute",
                            output_format="latex",
                        ),
                        "}",
                    ]
                ),
                "tex",
            )
        return None

    if (
        elem.tag == "Div"
        and elem.content
        and elem.content[0].tag == "Div"
        and "title" in elem.content[0].classes
        and elem.content[0].content[0].tag == "Para"
    ):
        elem.content[0].content[0].content.insert(
            0,
            RawInline(f"\\textbf{{\\color{{{environment['color']}}}", "tex"),
        )
        elem.content[0].content[0].content.append(RawInline("}", "tex"))

    images = []

    def extract_images(element, _doc):
        # Extract image which is alone with a title
        if isinstance(element, Figure) and len(element.content) == 1:
            images.append(element)
            return []
        return None

    # The images need to be placed after the framed environment
    return [
        RawBlock("\\begin{" + environment["env"] + "}", "tex"),
        elem.walk(extract_images).walk(note),
        RawBlock("\\end{" + environment["env"] + "}", "tex"),
    ] + images


def prepare(doc: Doc) -> None:
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    doc.x11colors = x11colors()

    # Prepare the definitions
    doc.defined = []
    doc.added = []

    # Get the meta data
    meta = doc.get_metadata("pandoc-latex-admonition")

    # pylint: disable=too-many-nested-blocks
    if isinstance(meta, list):
        # Loop on all definitions
        for definition in meta:
            # Verify the definition
            if (
                isinstance(definition, dict)
                and "classes" in definition
                and isinstance(definition["classes"], list)
            ):
                environment = define_environment(
                    doc,
                    definition,
                    "color",
                    "position",
                    "linewidth",
                    "margin",
                    "innermargin",
                    "localfootnotes",
                    "nobreak",
                )
                classes = []
                if all(isinstance(elem, str) for elem in definition["classes"]):
                    classes.append(set(definition["classes"]))
                else:
                    for elem in definition["classes"]:
                        if isinstance(elem, str):
                            classes.append({elem})
                        else:
                            classes.append({str(x) for x in elem})
                environment["classes"] = classes
                doc.defined.append(environment)


# pylint: disable=too-many-arguments,too-many-positional-arguments
def define_environment(
    doc: Doc,
    definition: dict[str, str],
    key_color: str,
    key_position: str,
    key_linewidth: str,
    key_margin: str,
    key_innermargin: str,
    key_localfootnotes: str,
    key_nobreak: str,
) -> dict[str, Any]:
    """
    Define a new environment.

    Arguments
    ---------
    doc
        The pandoc document

    definition
        The definition

    key_color
        The color key

    key_position
        The position key

    key_linewidth
        The linewidth key

    key_margin
        The margin key

    key_innermargin
        The innermargin key

    key_localfootnotes
        The localfootnotes key

    key_nobreak
        The nobreak key

    Returns
    -------
    dict[str, Any]
        A new environment
    """
    # Get the default environment
    environment = default_environment()
    define_color(environment, definition, key_color, doc=doc)
    define_position(environment, definition, key_position)
    define_linewidth(environment, definition, key_linewidth)
    define_margin(environment, definition, key_margin)
    define_innermargin(environment, definition, key_innermargin)
    define_localfootnotes(environment, definition, key_localfootnotes)
    define_nobreak(environment, definition, key_nobreak)
    return environment


def define_color(
    environment: dict[str, Any], definition: dict[str, str], key_color: str, doc: Doc
):
    """
    Define the color.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_color
        The color key

    doc
        The pandoc document
    """
    if key_color in definition:
        color = definition[key_color].lower()
        if color in doc.x11colors:
            environment["color"] = color
        else:
            # color must be a valid x11 color
            # See https://www.w3.org/TR/css-color-3/#svg-color
            debug(
                "[WARNING] pandoc-latex-admonition: "
                + color
                + " is not a valid x11 color; using "
                + environment["color"]
            )


def define_position(
    environment: dict[str, Any], definition: dict[str, str], key_position: str
) -> None:
    """
    Define the position.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_position
        The position key
    """
    if key_position in definition:
        environment["position"] = definition[key_position]


def define_linewidth(
    environment: dict[str, Any], definition: dict[str, str], key_linewidth: str
) -> None:
    """
    Define the line width.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_linewidth
        The linewidth key
    """
    if key_linewidth in definition:
        try:
            linewidth = int(definition[key_linewidth])
            if linewidth <= 0:
                debug(
                    "[WARNING] pandoc-latex-admonition: "
                    + "linewidth must be a positivie integer; using "
                    + str(environment["linewidth"])
                )
            else:
                environment["linewidth"] = linewidth
        except ValueError:
            debug(
                "[WARNING] pandoc-latex-admonition: linewidth is not a valid; using "
                + str(environment["linewidth"])
            )


def define_margin(
    environment: dict[str, Any], definition: dict[str, str], key_margin: str
) -> None:
    """
    Define the margin.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_margin
        The margin key
    """
    if key_margin in definition:
        try:
            environment["margin"] = int(definition[key_margin])
        except ValueError:
            debug(
                "[WARNING] pandoc-latex-admonition: margin is not a valid; using "
                + str(environment["margin"])
            )


def define_innermargin(
    environment: dict[str, Any], definition: dict[str, str], key_innermargin: str
) -> None:
    """
    Define the inner margin.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_innermargin
        The inner margin key
    """
    if key_innermargin in definition:
        try:
            environment["innermargin"] = int(definition[key_innermargin])
        except ValueError:
            debug(
                "[WARNING] pandoc-latex-admonition: innermargin is not a valid; using "
                + str(environment["innermargin"])
            )


def define_localfootnotes(
    environment: dict[str, Any], definition: dict[str, str], key_localfootnotes: str
) -> None:
    """
    Define the local footnotes.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_localfootnotes
        The localfootnotes key
    """
    if key_localfootnotes in definition:
        environment["localfootnotes"] = definition[key_localfootnotes].lower() == "true"


def define_nobreak(
    environment: dict[str, Any], definition: dict[str, str], key_nobreak: str
) -> None:
    """
    Define the nobreak.

    Arguments
    ---------
    environment
        The environment

    definition
        The definition

    key_nobreak
        The nobreak key
    """
    if key_nobreak in definition:
        environment["nobreak"] = (
            str(definition[key_nobreak]).lower() == "true"  # noqa: FURB123
        )


def new_environment(doc: Doc, environment: dict[str, Any]) -> str:
    """
    Create a new environment.

    Arguments
    ---------
    doc
        The pandoc document

    environment
        The environment

    Returns
    -------
    str
        The LaTeX environment
    """
    options = ["blanker"]

    if not environment["nobreak"]:
        options.append("breakable")
    if environment["position"] == "left":
        options.append(left_bar(environment))
    elif environment["position"] == "right":
        options.append(right_bar(environment))
    elif environment["position"] == "inner":
        options.append(
            f"if odd page={{{left_bar(environment)}}}{{{right_bar(environment)}}}"
        )
    elif environment["position"] == "outer":
        options.append(
            f"if odd page={{{right_bar(environment)}}}{{{left_bar(environment)}}}"
        )
    else:
        options.append(left_bar(environment))

    if environment["localfootnotes"] or doc.format == "beamer":
        return f"""
\\newenvironment{{{environment['env']}}}
{{
    \\tcolorbox[{','.join(options)}]
}}
{{
    \\endtcolorbox
}}
        """
    return f"""
\\newenvironment{{{environment['env']}}}
{{
    \\savenotes\\tcolorbox[{','.join(options)}]
    \\setcounter{{mpfootnote}}{{\\value{{footnote}}}}
    \\renewcommand\\thempfootnote{{\\arabic{{mpfootnote}}}}
}}
{{
    \\setcounter{{footnote}}{{\\value{{mpfootnote}}}}
    \\endtcolorbox\\spewnotes
}}
        """


def left_bar(environment: dict[str, Any]) -> str:
    """
    Generate a left bar.

    Arguments
    ---------
    environment
        The environment

    Returns
    -------
    str
        The left bar options
    """
    return bar(environment, "left", "west")


def right_bar(environment: dict[str, Any]) -> str:
    """
    Generate a right bar.

    Arguments
    ---------
    environment
        The environment

    Returns
    -------
    str
        The right bar options
    """
    return bar(environment, "right", "east")


# pylint: disable=blacklisted-name
def bar(environment: dict[str, Any], position: str, localization: str) -> str:
    """
    Generate a bar.

    Arguments
    ---------
    environment
        The environment

    position
        left or right

    localization
        east or west

    Returns
    -------
    str
        The bar options
    """
    return (
        f"{position}={environment['innermargin']:g}pt,borderline "
        f"{localization}={{{environment['linewidth']:g}pt}}"
        f"{{{environment['margin']:g}pt}}{{{environment['color']}}}"
    )


def finalize(doc: Doc) -> None:
    """
    Finalize the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # load 'footnote' or 'footnotehyper' package
    if doc.format == "latex":
        doc.metadata["tables"] = MetaBool(True)

    # Add header-includes if necessary
    if "header-includes" not in doc.metadata:
        doc.metadata["header-includes"] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata["header-includes"], MetaList):
        doc.metadata["header-includes"] = MetaList(doc.metadata["header-includes"])

    # Add useful LaTexPackage
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage{xcolor}", "tex"))
    )

    # Define x11 colors
    tex = [
        f"\\definecolor{{{name.lower()}}}{{HTML}}{{{color}}}"
        for name, color in doc.x11colors.items()
    ]
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\n".join(tex), "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage[most]{tcolorbox}", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(
            RawInline(
                r"""
\usepackage{ifthen}
\provideboolean{admonitiontwoside}
\makeatletter%
\if@twoside%
\setboolean{admonitiontwoside}{true}
\else%
\setboolean{admonitiontwoside}{false}
\fi%
\makeatother%
""",
                "tex",
            )
        )
    )
    # Define specific environments
    for environment in doc.defined + doc.added:
        doc.metadata["header-includes"].append(
            MetaInlines(RawInline(new_environment(doc, environment), "tex"))
        )


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
    Doc
        The modified pandoc document
    """
    return run_filter(admonition, prepare=prepare, finalize=finalize, doc=doc)


if __name__ == "__main__":
    main()
