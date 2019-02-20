.. pandoc-numbering documentation master file, created by
   sphinx-quickstart on Mon Dec 17 11:33:59 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pandoc-latex-admonition's documentation!
===================================================

Explanation
-----------

In the metadata block, specific set of classes can be defined to
decorate ``div`` or ``codeblock`` elements by admonition generated from
the ``tcolorbox`` LaTeX package

The metadata block add information using the ``pandoc-latex-admonition``
entry by a list of definitions:

::

   pandoc-latex-admonition:
   # order is important
     - color: firebrick
       classes: [admonition, danger]
     - color: gray
       classes: [admonition]

The metadata block above is used to add a ``red`` admonition to
``div``\ s or ``codeblock``\ s which have ``admonition`` and ``danger``
classes and a ``gray`` admonition to ``div``\ s or ``codeblock``\ s that
have only a ``admonition`` class.

Each entry of ``pandoc-latex-admonition`` is a YAML dictionary
containing:

-  ``classes``: the set of classes of the ``div``\ s to which the
   transformation will be applied. This parameter is mandatory.
-  ``color``: the color name taken from the `X11 color
   collection <https://www.w3.org/TR/css3-color/#svg-color>`__.
-  ``position``: the position of the admonition (``left`` by default or
   ``right``, ``inner``, ``outer``)
-  ``liwewidth`` the line width (2 by default)
-  ``margin`` the margin from the text (-4 by default)
-  ``innermargin`` the innermargin from the text (5 by default)
-  ``localfootnotes`` use local footnotes inside the admonition
   (``false`` by default)
-  ``nobreak`` force no break at end of pages

It’s also possible to set an admonition on a specific ``div`` or
``codeblock`` element using these attributes:

-  ``latex-admonition-color``: the color name taken from the `X11 color
   collection <https://www.w3.org/TR/css3-color/#svg-color>`__. This
   attribute is mandatory.
-  ``latex-admonition-position``: the position
   of the admonition (``left`` by default or ``right``, ``inner``, ``outer``)
-  ``latex-admonition-liwewidth`` the line width (2 by default)
-  ``latex-admonition-margin`` the margin from the text (-4 by default)
-  ``latex-admonition-innermargin`` the innermargin from the text (5 by
   default.)
-  ``latex-admonition-localfootnotes`` use local footnotes inside the
   admonition (``false`` by default)
-  ``latex-admonition-nobreak`` force no break at end of pages

For correct LaTeX output, figures (an image with nonempty alt text,
occurring by itself in a paragraph) must be shifted after the ``div``.

The following LaTeX packages are required:

-  ``tcolorbox``
-  ``xcolor``
-  ``footnote``
-  ``changepage``
-  ``ifthen``

Example
-------

Demonstration: Using
`pandoc-latex-admonition-sample.txt <https://raw.githubusercontent.com/chdemko/pandoc-latex-admonition/master/docs/images/pandoc-latex-admonition-sample.txt>`__
as input gives output file in
`pdf <https://raw.githubusercontent.com/chdemko/pandoc-latex-admonition/master/docs/images/pandoc-latex-admonition-sample.pdf>`__.
You must have the
`Markdown-mark.svg.png <https://raw.githubusercontent.com/chdemko/pandoc-latex-admonition/master/docs/images/Markdown-mark.svg.png>`__
image for correct testing.
