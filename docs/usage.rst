Usage
=====

To apply the filter, use the following option with pandoc:

.. code-block:: shell-session

    $ pandoc --filter pandoc-latex-admonition

Explanation
-----------

In the metadata block, specific set of classes can be defined to
decorate ``div`` or ``codeblock`` elements by admonition generated from
the ``tcolorbox`` LaTeX package

The metadata block add information using the ``pandoc-latex-admonition``
entry by a list of definitions:

.. code-block:: yaml

   pandoc-latex-admonition:
   # order is important
     - color: firebrick
       classes: [[admonition, danger]]
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
   It's either a list of strings and in this case, it represents the minimum
   set of of classes that the element must have, or it's either a list of
   sublists and each sublist represents the minimum set of classes that the
   element must have.
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
-  ``ifthen``

Example
-------

Demonstration: Using
:download:`pandoc-latex-admonition-sample.txt \
<images/pandoc-latex-admonition-sample.txt>`
as input gives output file in
:download:`pdf <images/pandoc-latex-admonition-sample.pdf>`.
You must have the
:download:`Markdown-mark.svg.png <images/Markdown-mark.svg.png>`
image for correct testing.
