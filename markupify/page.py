from typing import Optional, Union
from bs4 import BeautifulSoup

from .tags import Element, Html, Head, Body, DocType


class HTMLPage:
    """
    Page template class to make an HTML page.

    Args:
        lang (str, optional): The language of the HTML page (Defaults to "en").

    Attributes:
        lang (str): The language of the HTML page.

    Methods:
        __init__: Initialize the HTMLPage instance.
        __str__: Return a string representation of the HTMLPage.
        __repr__: Return a string representation of the HTMLPage.
        render: Render the HTML content of the page.
        doc_type: Get the DocType of the HTML page.
        html: Get the Html element of the HTML page.
        set_head: Set the head section of the HTML page.
        set_body: Set the body section of the HTML page.
        pretty: Prettify the HTML content.
        add_head: Add tags to the head section.
        add_body: Add tags to the body section.
    """

    def __init__(self, lang: str = "en"):
        """
        Initialize the HTMLPage instance.

        Args:
            lang (str, optional): The language of the HTML page (Defaults to "en").
        """
        self.lang: str = lang
        self.template: str = "{doc_type}{html}"
        self._head: Head = self.set_head()
        self._body: Body = self.set_body()

    def __str__(self) -> str:
        """
        Return a string representation of the HTMLPage.

        Returns:
            str: The HTML content of the page.
        """
        return self.render()

    def __repr__(self) -> str:
        """
        Return a string representation of the HTMLPage.

        Returns:
            str: The HTML content of the page.
        """
        return self.render()

    def render(self) -> str:
        """
        Render the HTML content of the page.

        Returns:
            str: The HTML content of the page.
        """
        return self.template.format(doc_type=self.doc_type, html=self.html)

    @property
    def doc_type(self) -> DocType:
        """
        Get the DocType of the HTML page.

        Returns:
            DocType: The DocType of the HTML page.
        """
        doc_type = DocType("html")
        return doc_type

    @property
    def html(self) -> Html:
        """
        Get the Html element of the HTML page.

        Returns:
            Html: The Html element of the HTML page.
        """
        html = Html(
            tag_content=f"{self._head}{self._body}",
            lang=self.lang,
        )
        return html

    def set_head(self, *args, **props) -> Head:
        """
        Set the head section of the HTML page.

        Args:
            *args (Any, optional): The list of contents of the head section (Defaults to "").
            **props: Additional properties for the head section.

        Returns:
            Head: The Head element of the HTML page.
        """
        content = ""
        for tag in args:
            content += str(tag)
        self._head = Head(tag_content=content, **props)
        return self._head

    def set_body(self, *args, **props) -> Body:
        """
        Set the body section of the HTML page.

        Args:
            *args (Any, optional): The list of contents of the body section (Defaults to "").
            **props: Additional properties for the body section.

        Returns:
            Body: The Body element of the HTML page.
        """
        content = ""
        for tag in args:
            content += str(tag)
        self._body = Body(tag_content=content, **props)
        return self._body

    def pretty(self, html_content: Optional[Union[str, Element]] = "", encoding=None, formatter="minimal") -> str:
        """
        Prettify the HTML content.

        Args:
            html_content (str, optional): The HTML content to be prettified (Defaults to "").
            encoding: Encoding to use for prettifying (Defaults to None).
            formatter (str, optional): The formatter to use for prettifying (Defaults to "minimal").

        Returns:
            str: The prettified HTML content.
        """
        if not html_content:
            html_content = self.render()

        soup = BeautifulSoup(html_content, "html.parser")
        return soup.prettify(encoding, formatter)

    def add_tag_to_head(self, *args) -> Head:
        """
        Add tags to the head section of the HTML page.

        Args:
            *args (Any): The list of contents to be added to the head section.
        """
        for tag in args:
            self._head.tag_content += str(tag)
        return self._head

    def add_tag_to_body(self, *args) -> Body:
        """
        Add tags to the body section of the HTML page.

        Args:
            *args (Any): The list of contents to be added to the body section.
        """
        for tag in args:
            self._body.tag_content += str(tag)
        return self._body
