from .tags import Html, Head, Body, DocType


class HTMLPage:
    """
    Page template class to make an HTML page.
    """

    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.template = "<!DOCTYPE html>{html}"

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()

    def render(self) -> str:
        return self.template.format(html=self.html)

    @property
    def html(self) -> Html:
        html = Html(
            content=f"{self.head}{self.body}",
            lang=self.lang,
        )

        return html

    @property
    def doc_type(self) -> DocType:
        doc_type = DocType("html")
        return doc_type

    @property
    def head(self) -> Head:
        head = Head()
        return head

    @property
    def body(self) -> Body:
        body = Body()
        return body

    @property
    def pretty(self):
        indent_size = 4
        indentation = 0
        formatted_html = ""

        tokens = self.render().split("<")

        for token in tokens:
            if token.strip() == "":
                continue

            if token.startswith("/"):
                indentation -= 1

            if token.startswith("html") or token.startswith("/html"):
                formatted_html += "\n"
            else:
                formatted_html += "\n" + " " * (indent_size * indentation)

            formatted_html += "<" + token

            if not token.endswith("/>") and not token.startswith("/"):
                indentation += 1

        return formatted_html.strip()
