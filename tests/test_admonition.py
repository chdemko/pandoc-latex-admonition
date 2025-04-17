from unittest import TestCase

from panflute import convert_text, Para, Image, Figure

import pandoc_latex_admonition


class AdmonitionTest(TestCase):
    @classmethod
    def conversion(cls, markdown, fmt="markdown"):
        doc = convert_text(markdown, standalone=True)
        doc.format = fmt
        pandoc_latex_admonition.main(doc)
        return doc

    def test_codeblock_classes(self):
        doc = AdmonitionTest.conversion(
            """
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
            """,
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertIn("\\begin{env-", text)
        self.assertIn(
            r"\tcolorbox[blanker,breakable,right=-8pt,borderline east={5pt}{10pt}{red}]",
            doc.get_metadata()["header-includes"][-1],
        )

    def test_codeblock_attributes(self):
        doc = AdmonitionTest.conversion(
            """
::: {latex-admonition-color=xyz latex-admonition-linewidth=xyz latex-admonition-margin=xyz latex-admonition-innermargin=xyz latex-admonition-localfootnotes=true} :::
:::::::::
            """,
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertIn("\\begin{env-", text)
        self.assertIn("\\end{env-", text)
        self.assertIn(
            r"\tcolorbox[blanker,breakable,left=5pt,borderline west={2pt}{-4pt}{black}]",
            doc.get_metadata()["header-includes"][-1],
        )

    def test_latex_images(self):
        doc = AdmonitionTest.conversion(
            """\
::: {latex-admonition-color=black} :::

![Title]()

Hello
:::::::::
            """.strip(),
            "latex",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )

        self.assertIn("\\begin{env-", text)
        self.assertIn("\\end{env-", text)
        self.assertIn(
            r"\tcolorbox[blanker,breakable,left=5pt,borderline west={2pt}{-4pt}{black}]",
            doc.get_metadata()["header-includes"][-1],
        )
        self.assertIsInstance(doc.content[-1], Figure)

    def test_beamer_notes(self):
        doc = AdmonitionTest.conversion(
            """
::: {latex-admonition-color=black} :::

This a text[^note]

[^note]: This is a *note*

:::
            """,
            "beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="beamer",
            extra_args=["--wrap=none"],
        )
        self.assertIn("This a text\\footnote<.->[frame]{This is a \\emph{note}}", text)
