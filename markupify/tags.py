from typing import Iterable, Optional, Union


class Element:
    """
    The base class to make an HTML element.

    Args:
        tag_name (str): The tag name.
        has_end_tag (bool, optional): If set to False, the tag will not contain content and end tag. Default: True.
        *tags (str or Element): The list of tags to make content of the tag.
        **props: Properties for the tag.

    Methods:
        __init__: Initialize the Element instance.
        __str__: Return a string representation of the Element.
        __repr__: Return a string representation of the Element.
        __add__: Concatenate tag content when using the addition operator.
        render: Render the HTML content of the tag.
        add_property: Add a property to the tag.
        add_properties: Add multiple properties to the tag.
        add_style: Add a style to the tag.
        add_styles: Add multiple styles to the tag.
        add_content: Add content to the tag.
        text: Get the text content of the tag.
    """

    def __init__(
        self,
        tag_name: Optional[str] = "div",
        has_end_tag: Optional[bool] = True,
        *tags: Optional[str, "Element"],
        **props: object,
    ) -> None:
        """
        Initialize the Element instance.

        Args:
            tag_name (str, optional): The tag name. Defaults to "div".
            has_end_tag (bool, optional): If set to False, the tag will not contain content and end tag. Default: True.
            *tags (str or Element): The list of tags to make content of the tag. Defaults to "".
            **props: Properties for the tag.
        """
        if not has_end_tag and tags:
            raise ValueError(
                "Tags without end parts cannot contain content. "
                "Set has_end_tag to True or leave blank the *tags."
            )

        self.tag_name = tag_name.lower()
        self.has_end_tag = has_end_tag
        self.tag_content = "".join(tags)
        self.properties = props

        self.props = ""
        self.style = ""

        style_property = self.properties.pop("style", None)
        if style_property:
            if isinstance(style_property, str):
                self.style += style_property
            elif isinstance(style_property, dict):
                self.add_styles(**style_property)
            else:
                raise TypeError("style property must be string or dict.")

        if self.style:
            self.add_property("style", self.style)
        self.add_properties(**self.properties)

    def __str__(self) -> str:
        """
        Return a string representation of the Element.

        Returns:
            str: The string representation of the Element.
        """
        return self.render()

    def __repr__(self) -> str:
        """
        Return a string representation of the Element.

        Returns:
            str: The string representation of the Element.
        """
        return self.render()

    def __add__(self, other: Union[str, "Element"]) -> "Element":
        """
        Concatenate tag content when using the addition operator.

        Args:
            other: The content to concatenate with the current tag content.

        Returns:
            Element: A new Element instance with concatenated tag content.
        """
        new_tag_content = str(self.tag_content) + str(other)
        return Element(
            tag_name=self.tag_name,
            has_end_tag=self.has_end_tag,
            tag_content=new_tag_content,
            **self.properties,
        )

    def render(self) -> str:
        """
        Render the HTML content of the tag.

        Returns:
            str: The HTML content of the tag.
        """
        structure = "<{tag_name}"

        if self.props:
            structure += " {props}"
        if self.has_end_tag:
            structure += ">"
        if self.tag_content:
            structure += "{tag_content}"

        if self.has_end_tag:
            structure += "</{tag_name}>"
        elif not self.has_end_tag:
            structure += " />"

        return structure.format(
            tag_name=self.tag_name,
            props=self.props.strip(),
            tag_content=self.tag_content,
        )

    def add_property(self, name: str, value: str) -> None:
        """
        Add a property to the tag.

        Args:
            name (str): The name of the property.
            value (str): The value of the property.
        """
        self.props += f'{name}="{value}" '

    def add_properties(self, **props) -> None:
        """
        Add multiple properties to the tag.

        Args:
            **props: Properties for the tag.
        """
        for name, value in props.items():
            name = name.strip("_")
            name = name.replace("_", "-")
            self.add_property(name, value)

    def add_style(self, name: str, value: str) -> None:
        """
        Add a style to the tag.

        Args:
            name (str): The name of the style.
            value (str): The value of the style.
        """
        self.style += f"{name}: {value};"

    def add_styles(self, **styles) -> None:
        """
        Add multiple styles to the tag.

        Args:
            **styles: Styles for the tag.
        """
        for name, value in styles.items():
            name = name.strip("_")
            name = name.replace("_", "-")
            self.add_style(name, value)

    def add_content(self, *tags: Union[str, "Element"]) -> None:
        """
        Add content to the tag.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the tag.
        """
        self.tag_content += "".join(tags)

    @property
    def text(self) -> [str, "Element"]:
        """
        Get the text content of the tag.

        Returns:
            [str, 'Element']: The text content of the tag.
        """
        return self.tag_content


class A(Element):
    """
    Represents the <a> HTML element.
    """

    def __init__(
        self,
        link: str,
        *tags: Union[Iterable[str], Iterable[Element]],
        **props,
    ):
        """
        Initialize the A element.

        Args:
            link (str): The URL the hyperlink points to.
            *tags (str, Element): The list of tags to make content to be added to the <a> tag.
            **props: Additional properties for the <a> tag.
        """
        super().__init__(tag_name="a", *tags, href=link, **props)


class Abbr(Element):
    """
    Represents the <abbr> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Abbr element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <abbr> tag.
            **props: Additional properties for the <abbr> tag.
        """
        super().__init__(tag_name="abbr", *tags, **props)


class Address(Element):
    """
    Represents the <address> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Address element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <address> tag.
            **props: Additional properties for the <address> tag.
        """
        super().__init__(tag_name="address", *tags, **props)


class Area(Element):
    """
    Represents the <area> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Area element.

        Args:
            **props: Additional properties for the <area> tag.
        """
        super().__init__(tag_name="area", has_end_tag=False, **props)


class Article(Element):
    """
    Represents the <article> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Article element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <article> tag.
            **props: Additional properties for the <article> tag.
        """
        super().__init__(tag_name="article", *tags, **props)


class Aside(Element):
    """
    Represents the <aside> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Aside element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <aside> tag.
            **props: Additional properties for the <aside> tag.
        """
        super().__init__(tag_name="aside", *tags, **props)


class Audio(Element):
    """
    Represents the <audio> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Audio element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <audio> tag.
            **props: Additional properties for the <audio> tag.
        """
        super().__init__(tag_name="audio", *tags, **props)


class B(Element):
    """
    Represents the <b> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the B element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <b> tag.
            **props: Additional properties for the <b> tag.
        """
        super().__init__(tag_name="b", *tags, **props)


class Base(Element):
    """
    Represents the <base> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Base element.

        Args:
            **props: Additional properties for the <base> tag.
        """
        super().__init__(tag_name="base", has_end_tag=False, **props)


class Bdi(Element):
    """
    Represents the <bdi> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Bdi element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <bdi> tag.
            **props: Additional properties for the <bdi> tag.
        """
        super().__init__(tag_name="bdi", *tags, **props)


class Bdo(Element):
    """
    Represents the <bdo> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Bdo element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <bdo> tag.
            **props: Additional properties for the <bdo> tag.
        """
        super().__init__(tag_name="bdo", *tags, **props)


class BlockQuote(Element):
    """
    Represents the <blockquote> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the BlockQuote element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <blockquote> tag.
            **props: Additional properties for the <blockquote> tag.
        """
        super().__init__(tag_name="blockquote", *tags, **props)


class Body(Element):
    """
    Represents the <body> HTML element.
    """

    def __init__(self, *tags: Union[str, "Element"], **props):
        """
        Initialize the Body element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <body> tag.
            **props: Additional properties for the <body> tag.
        """
        super().__init__(tag_name="body", *tags, **props)


class Br(Element):
    """
    Represents the <br> HTML element.
    """

    def __init__(self):
        """
        Initialize the Br element.
        """
        super().__init__(tag_name="br", has_end_tag=False)


class Button(Element):
    """
    Represents the <button> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Button element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <button> tag.
            **props: Additional properties for the <button> tag.
        """
        super().__init__(tag_name="button", *tags, **props)


class Canvas(Element):
    """
    Represents the <canvas> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Canvas element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <canvas> tag.
            **props: Additional properties for the <canvas> tag.
        """
        super().__init__(tag_name="canvas", *tags, **props)


class Caption(Element):
    """
    Represents the <caption> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Caption element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <caption> tag.
            **props: Additional properties for the <caption> tag.
        """
        super().__init__(tag_name="caption", *tags, **props)


class Circle(Element):
    """
    Represents the <circle> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Circle element.

        Args:
            **props: Additional properties for the <circle> tag.
        """
        super().__init__(tag_content="circle", has_end_tag=False, **props)


class Cite(Element):
    """
    Represents the <cite> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Cite element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <cite> tag.
            **props: Additional properties for the <cite> tag.
        """
        super().__init__(tag_name="cite", *tags, **props)


class Code(Element):
    """
    Represents the <code> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Code element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <code> tag.
            **props: Additional properties for the <code> tag.
        """
        super().__init__(tag_name="code", *tags, **props)


class Col(Element):
    """
    Represents the <col> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Col element.

        Args:
            **props: Additional properties for the <col> tag.
        """
        super().__init__(tag_content="col", has_end_tag=False, **props)


class ColGroup(Element):
    """
    Represents the <colgroup> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the ColGroup element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <colgroup> tag.
            **props: Additional properties for the <colgroup> tag.
        """
        super().__init__(tag_name="colgroup", *tags, **props)


class Comment:
    """
    Represents an HTML comment.
    """

    def __init__(
        self,
        *tags: Union[Iterable[str], Iterable[Element]],
    ):
        """
        Initialize the Comment.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the comment.
        """
        self.tag_content = ""
        for tag in tags:
            self.tag_content += tag
        self.multiline = bool(len(tags) > 1)

    def __str__(self) -> str:
        """
        Return a string representation of the comment.

        Returns:
            str: The string representation of the comment.
        """
        return self.render()

    def __repr__(self) -> str:
        """
        Return a string representation of the comment.

        Returns:
            str: The string representation of the comment.
        """
        return self.render()

    def render(self) -> str:
        """
        Render the comment.

        Returns:
            str: The rendered comment.
        """
        if self.multiline:
            return f"""
            <!--
                {self.tag_content}
            -->
            """.strip()
        return f"<!-- {self.tag_content} -->"


class Data(Element):
    """
    Represents the <data> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Data element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <data> tag.
            **props: Additional properties for the <data> tag.
        """
        super().__init__(tag_name="data", *tags, **props)


class DataIterable(Element):
    """
    Represents the <datalist> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the DataIterable element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <datalist> tag.
            **props: Additional properties for the <datalist> tag.
        """
        super().__init__(tag_name="datalist", *tags, **props)


class Dd(Element):
    """
    Represents the <dd> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Dd element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <dd> tag.
            **props: Additional properties for the <dd> tag.
        """
        super().__init__(tag_name="dd", *tags, **props)


class Defs(Element):
    """
    Represents the <defs> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Defs element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <defs> tag.
            **props: Additional properties for the <defs> tag.
        """
        super().__init__(tag_name="defs", *tags, **props)


class Del(Element):
    """
    Represents the <del> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Del element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <del> tag.
            **props: Additional properties for the <del> tag.
        """
        super().__init__(tag_name="del", *tags, **props)


class Details(Element):
    """
    Represents the <details> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Details element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <details> tag.
            **props: Additional properties for the <details> tag.
        """
        super().__init__(tag_name="details", *tags, **props)


class Dfn(Element):
    """
    Represents the <dfn> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Dfn element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <dfn> tag.
            **props: Additional properties for the <dfn> tag.
        """
        super().__init__(tag_name="dfn", *tags, **props)


class Dialog(Element):
    """
    Represents the <dialog> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Dialog element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <dialog> tag.
            **props: Additional properties for the <dialog> tag.
        """
        super().__init__(tag_name="dialog", *tags, **props)


class Div(Element):
    """
    Represents the <div> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Div element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <div> tag.
            **props: Additional properties for the <div> tag.
        """
        super().__init__(tag_name="div", *tags, **props)


class Dl(Element):
    """
    Represents the <dl> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Dl element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <dl> tag.
            **props: Additional properties for the <dl> tag.
        """
        super().__init__(tag_name="dl", *tags, **props)


class DocType:
    """
    Represents the document type declaration (DOCTYPE) of an HTML document.
    """

    def __init__(self, doc_type: str = "html"):
        """
        Initialize the DocType.

        Args:
            doc_type (str, optional): The type of the document (Defaults to "html").
        """
        self.doc_type = doc_type

    def __str__(self) -> str:
        """
        Return a string representation of the DocType.

        Returns:
            str: The string representation of the DocType.
        """
        return self.render()

    def __repr__(self) -> str:
        """
        Return a string representation of the DocType.

        Returns:
            str: The string representation of the DocType.
        """
        return self.render()

    def render(self) -> str:
        """
        Render the DocType.

        Returns:
            str: The rendered DocType.
        """
        return f"<!DOCTYPE {self.doc_type}>"


class Dt(Element):
    """
    Represents the <dt> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Dt element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <dt> tag.
            **props: Additional properties for the <dt> tag.
        """
        super().__init__(tag_name="dt", *tags, **props)


class Ellipse(Element):
    """
    Represents the <ellipse> SVG element.
    """

    def __init__(self, **props):
        """
        Initialize the Ellipse element.

        Args:
            **props: Additional properties for the <ellipse> tag.
        """
        super().__init__(tag_name="ellipse", has_end_tag=False, **props)


class Em(Element):
    """
    Represents the <em> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Em element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <em> tag.
            **props: Additional properties for the <em> tag.
        """
        super().__init__(tag_name="em", *tags, **props)


class Embed(Element):
    """
    Represents the <embed> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Embed element.

        Args:
            **props: Additional properties for the <embed> tag.
        """
        super().__init__(tag_name="embed", has_end_tag=False, **props)


class FieldSet(Element):
    """
    Represents the <fieldset> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the FieldSet element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <fieldset> tag.
            **props: Additional properties for the <fieldset> tag.
        """
        super().__init__(tag_name="fieldset", *tags, **props)


class FigCaption(Element):
    """
    Represents the <figcaption> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the FigCaption element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <figcaption> tag.
            **props: Additional properties for the <figcaption> tag.
        """
        super().__init__(tag_name="figcaption", *tags, **props)


class Figure(Element):
    """
    Represents the <figure> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Figure element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <figure> tag.
            **props: Additional properties for the <figure> tag.
        """
        super().__init__(tag_name="figure", *tags, **props)


class Footer(Element):
    """
    Represents the <footer> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Footer element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <footer> tag.
            **props: Additional properties for the <footer> tag.
        """
        super().__init__(tag_name="footer", *tags, **props)


class Form(Element):
    """
    Represents the <form> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Form element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <form> tag.
            **props: Additional properties for the <form> tag.
        """
        super().__init__(tag_name="form", *tags, **props)


class H(Element):
    """
    Represents a heading (h1 - h6) HTML element.
    """

    def __init__(
        self,
        level: int = 1,
        *tags: Union[Iterable[str], Iterable[Element]],
        **props,
    ):
        """
        Initialize the H element.

        Args:
            level (int): The level of the heading (1-6).
            *tags (str, Element): The list of tags to make content to be added to the <h1>-<h6> tag.
            **props: Additional properties for the heading tag.
        """
        if not 1 <= level <= 6:
            raise ValueError(
                "The heading level must be an integer in range 1-6."
            )
        super().__init__(tag_name=f"h{level}", *tags, **props)


class Head(Element):
    """
    Represents the <head> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the head element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <head> tag.
            **props: Additional properties for the <head> tag.
        """
        super().__init__(tag_name="head", *tags, **props)


class Header(Element):
    """
    Represents the <header> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Header element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <header> tag.
            **props: Additional properties for the <header> tag.
        """
        super().__init__(tag_name="header", *tags, **props)


class HGroup(Element):
    """
    Represents the <hgroup> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the HGroup element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <hgroup> tag.
            **props: Additional properties for the <hgroup> tag.
        """
        super().__init__(tag_name="hgroup", *tags, **props)


class Hr(Element):
    """
    Represents the <hr> HTML element.
    """

    def __init__(self):
        """
        Initialize the Hr element.
        """
        super().__init__(tag_name="hr", has_end_tag=False)


class Html(Element):
    """
    Represents the <html> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Html element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <html> tag.
            **props: Additional properties for the <html> tag.
        """
        super().__init__(tag_name="html", *tags, **props)


class I(Element):
    """
    Represents the <i> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the i element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <i> tag.
            **props: Additional properties for the <i> tag.
        """
        super().__init__(tag_name="i", *tags, **props)


class IFrame(Element):
    """
    Represents the <iframe> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the IFrame element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <iframe> tag.
            **props: Additional properties for the <iframe> tag.
        """
        super().__init__(tag_name="iframe", *tags, **props)


class Img(Element):
    """
    Represents the <img> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Img element.

        Args:
            src (str): The source URL of the image.
            **props: Additional properties for the <img> tag.
        """
        super().__init__(tag_name="img", has_end_tag=False, **props)


class Input(Element):
    """
    Represents the <input> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Input element.

        Args:
            **props: Additional properties for the <input> tag.
        """
        super().__init__(tag_name="input", has_end_tag=False, **props)


class Ins(Element):
    """
    Represents the <ins> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Ins element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <ins> tag.
            **props: Additional properties for the <ins> tag.
        """
        super().__init__(tag_name="ins", *tags, **props)


class Kbd(Element):
    """
    Represents the <kbd> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Kbd element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <kbd> tag.
            **props: Additional properties for the <kbd> tag.
        """
        super().__init__(tag_name="kbd", *tags, **props)


class Label(Element):
    """
    Represents the <label> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Label element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <label> tag.
            **props: Additional properties for the <label> tag.
        """
        super().__init__(tag_name="label", *tags, **props)


class Legend(Element):
    """
    Represents the <legend> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Legend element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <legend> tag.
            **props: Additional properties for the <legend> tag.
        """
        super().__init__(tag_name="legend", *tags, **props)


class Li(Element):
    """
    Represents the <li> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Li element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <li> tag.
            **props: Additional properties for the <li> tag.
        """
        super().__init__(tag_name="li", *tags, **props)


class LinearGradient(Element):
    """
    Represents the <linearGradient> SVG element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the LinearGradient element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <linearGradient> tag.
            **props: Additional properties for the <linearGradient> tag.
        """
        super().__init__(tag_name="linearGradient", *tags, **props)


class Link(Element):
    """
    Represents the <link> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Link element.

        Args:
            **props: Additional properties for the <link> tag.
        """
        super().__init__(tag_name="link", has_end_tag=False, **props)


class Main(Element):
    """
    Represents the <main> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Main element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <main> tag.
            **props: Additional properties for the <main> tag.
        """
        super().__init__(tag_name="main", *tags, **props)


class Map(Element):
    """
    Represents the <map> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Map element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <map> tag.
            **props: Additional properties for the <map> tag.
        """
        super().__init__(tag_name="map", *tags, **props)


class Mark(Element):
    """
    Represents the <mark> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Mark element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <mark> tag.
            **props: Additional properties for the <mark> tag.
        """
        super().__init__(tag_name="mark", *tags, **props)


class Menu(Element):
    """
    Represents the <menu> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Menu element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <menu> tag.
            **props: Additional properties for the <menu> tag.
        """
        super().__init__(tag_name="menu", *tags, **props)


class Meta(Element):
    """
    Represents the <meta> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Meta element.

        Args:
            **props: Additional properties for the <meta> tag.
        """
        super().__init__(tag_name="meta", has_end_tag=False, **props)


class Meter(Element):
    """
    Represents the <meter> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Meter element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <meter> tag.
            **props: Additional properties for the <meter> tag.
        """
        super().__init__(tag_name="meter", *tags, **props)


class Nav(Element):
    """
    Represents the <nav> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Nav element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <nav> tag.
            **props: Additional properties for the <nav> tag.
        """
        super().__init__(tag_name="nav", *tags, **props)


class NoScript(Element):
    """
    Represents the <noscript> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the NoScript element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <noscript> tag.
            **props: Additional properties for the <noscript> tag.
        """
        super().__init__(tag_name="noscript", *tags, **props)


class Object(Element):
    """
    Represents the <object> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Object element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <object> tag.
            **props: Additional properties for the <object> tag.
        """
        super().__init__(tag_name="option", *tags, **props)


class Ol(Element):
    """
    Represents the <ol> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Ol element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <ol> tag.
            **props: Additional properties for the <ol> tag.
        """
        super().__init__(tag_name="ol", *tags, **props)


class OptGroup(Element):
    """
    Represents the <optgroup> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the OptGroup element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <optgroup> tag.
            **props: Additional properties for the <optgroup> tag.
        """
        super().__init__(tag_name="optgroup", *tags, **props)


class Option(Element):
    """
    Represents the <option> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Option element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <option> tag.
            **props: Additional properties for the <option> tag.
        """
        super().__init__(tag_name="option", *tags, **props)


class Output(Element):
    """
    Represents the <output> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Output element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <output> tag.
            **props: Additional properties for the <output> tag.
        """
        super().__init__(tag_name="output", *tags, **props)


class P(Element):
    """
    Represents the <p> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the P element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <p> tag.
            **props: Additional properties for the <p> tag.
        """
        super().__init__(tag_name="p", *tags, **props)


class Param(Element):
    """
    Represents the <param> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Param element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <param> tag.
            **props: Additional properties for the <param> tag.
        """
        super().__init__(tag_name="param", *tags, **props)


class Picture(Element):
    """
    Represents the <picture> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Picture element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <picture> tag.
            **props: Additional properties for the <picture> tag.
        """
        super().__init__(tag_name="picture", *tags, **props)


class Polygon(Element):
    """
    Represents the <polygon> SVG element.
    """

    def __init__(self, **props):
        """
        Initialize the Polygon element.

        Args:
            **props: Additional properties for the <polygon> tag.
        """
        super().__init__(tag_name="polygon", has_end_tag=False, **props)


class Pre(Element):
    """
    Represents the <pre> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Pre element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <pre> tag.
            **props: Additional properties for the <pre> tag.
        """
        super().__init__(tag_name="pre", *tags, **props)


class Progress(Element):
    """
    Represents the <progress> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Progress element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <progress> tag.
            **props: Additional properties for the <progress> tag.
        """
        super().__init__(tag_name="progress", *tags, **props)


class Q(Element):
    """
    Represents the <q> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Q element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <q> tag.
            **props: Additional properties for the <q> tag.
        """
        super().__init__(tag_name="q", *tags, **props)


class Rect(Element):
    """
    Represents the <rect> SVG element.
    """

    def __init__(self, **props):
        """
        Initialize the Rect element.

        Args:
            **props: Additional properties for the <rect> tag.
        """
        super().__init__(tag_name="rect", has_end_tag=False, **props)


class Rp(Element):
    """
    Represents the <rp> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Rp element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <rp> tag.
            **props: Additional properties for the <rp> tag.
        """
        super().__init__(tag_name="rp", *tags, **props)


class Rt(Element):
    """
    Represents the <rt> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Rt element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <rt> tag.
            **props: Additional properties for the <rt> tag.
        """
        super().__init__(tag_name="rt", *tags, **props)


class Ruby(Element):
    """
    Represents the <ruby> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Ruby element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <ruby> tag.
            **props: Additional properties for the <ruby> tag.
        """
        super().__init__(tag_name="ruby", *tags, **props)


class S(Element):
    """
    Represents the <s> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the S element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <s> tag.
            **props: Additional properties for the <s> tag.
        """
        super().__init__(tag_name="s", *tags, **props)


class Samp(Element):
    """
    Represents the <samp> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Samp element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <samp> tag.
            **props: Additional properties for the <samp> tag.
        """
        super().__init__(tag_name="samp", *tags, **props)


class Script(Element):
    """
    Represents the <script> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Script element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <script> tag.
            **props: Additional properties for the <script> tag.
        """
        super().__init__(tag_name="script", *tags, **props)


class Search(Element):
    """
    Represents the <search> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Search element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <search> tag.
            **props: Additional properties for the <search> tag.
        """
        super().__init__(tag_name="search", *tags, **props)


class Section(Element):
    """
    Represents the <section> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Section element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <section> tag.
            **props: Additional properties for the <section> tag.
        """
        super().__init__(tag_name="section", *tags, **props)


class Select(Element):
    """
    Represents the <select> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Select element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <select> tag.
            **props: Additional properties for the <select> tag.
        """
        super().__init__(tag_name="select", *tags, **props)


class Small(Element):
    """
    Represents the <small> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Small element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <small> tag.
            **props: Additional properties for the <small> tag.
        """
        super().__init__(tag_name="small", *tags, **props)


class Source(Element):
    """
    Represents the <source> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Source element.

        Args:
            **props: Additional properties for the <source> tag.
        """
        super().__init__(tag_name="source", has_end_tag=False, **props)


class Span(Element):
    """
    Represents the <span> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Span element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <span> tag.
            **props: Additional properties for the <span> tag.
        """
        super().__init__(tag_name="span", *tags, **props)


class Stop(Element):
    """
    Represents the <stop> SVG element.
    """

    def __init__(self, **props):
        """
        Initialize the Stop element.

        Args:
            **props: Additional properties for the <stop> tag.
        """
        super().__init__(tag_name="stop", has_end_tag=False, **props)


class Strong(Element):
    """
    Represents the <strong> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Strong element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <strong> tag.
            **props: Additional properties for the <strong> tag.
        """
        super().__init__(tag_name="strong", *tags, **props)


class Style(Element):
    """
    Represents the <style> HTML element.
    """

    def __init__(self, **props):
        """
        Initialize the Style element.

        Args:
            **props: Additional properties for the <style> tag.
        """
        tag_content = ""
        for key, value in props.items():
            if isinstance(value, dict):
                val = "".join(
                    f"{k.replace('_', '-')}: {v};" for k, v in value.items()
                )
                tag_content += f"{key} {val}"
            elif isinstance(value, str):
                tag_content += f"{key} {value}"

            else:
                raise TypeError("property must be string or dict.")
        super().__init__(tag_name="style", tags=(tag_content,), **props)


class Sub(Element):
    """
    Represents the <sub> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the <sub> element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <sub> tag.
            **props: Additional properties for the <sub> tag.
        """
        super().__init__(tag_name="sub", *tags, **props)


class Summary(Element):
    """
    Represents the <summary> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Summary element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <summary> tag.
            **props: Additional properties for the <summary> tag.
        """
        super().__init__(tag_name="summary", *tags, **props)


class Sup(Element):
    """
    Represents the <sup> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Sup element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <sup> tag.
            **props: Additional properties for the <sup> tag.
        """
        super().__init__(tag_name="sup", *tags, **props)


class Svg(Element):
    """
    Represents the <svg> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Svg element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <svg> tag.
            **props: Additional properties for the <svg> tag.
        """
        super().__init__(tag_name="svg", *tags, **props)


class Table(Element):
    """
    Represents the <table> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Table element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <table> tag.
            **props: Additional properties for the <table> tag.
        """
        super().__init__(tag_name="table", *tags, **props)


class TBody(Element):
    """
    Represents the <tbody> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the TBody element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <tbody> tag.
            **props: Additional properties for the <tbody> tag.
        """
        super().__init__(tag_name="tbody", *tags, **props)


class Td(Element):
    """
    Represents the <td> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Td element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <td> tag.
            **props: Additional properties for the <td> tag.
        """
        super().__init__(tag_name="td", *tags, **props)


class Template(Element):
    """
    Represents the <template> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Template element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <template> tag.
            **props: Additional properties for the <template> tag.
        """
        super().__init__(tag_name="template", *tags, **props)


class Text(Element):
    """
    Represents the <text> SVG element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Text element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <text> tag.
            **props: Additional properties for the <text> tag.
        """
        super().__init__(tag_name="text", *tags, **props)


class Textarea(Element):
    """
    Represents the <textarea> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Textarea element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <textarea> tag.
            **props: Additional properties for the <textarea> tag.
        """
        super().__init__(tag_name="textarea", *tags, **props)


class TFoot(Element):
    """
    Represents the <tfoot> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the TFoot element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <tfoot> tag.
            **props: Additional properties for the <tfoot> tag.
        """
        super().__init__(tag_name="tfoot", *tags, **props)


class Th(Element):
    """
    Represents the <th> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the th element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <th> tag.
            **props: Additional properties for the <th> tag.
        """
        super().__init__(tag_name="th", *tags, **props)


class THead(Element):
    """
    Represents the <thead> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the THead element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <thead> tag.
            **props: Additional properties for the <thead> tag.
        """
        super().__init__(tag_name="thead", *tags, **props)


class Time(Element):
    """
    Represents the <time> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Time element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <time> tag.
            **props: Additional properties for the <time> tag.
        """
        super().__init__(tag_name="time", *tags, **props)


class Title(Element):
    """
    Represents the <title> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Title element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <title> tag.
            **props: Additional properties for the <title> tag.
        """
        super().__init__(tag_name="title", *tags, **props)


class Tr(Element):
    """
    Represents the <tr> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the tr element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <tr> tag.
            **props: Additional properties for the <tr> tag.
        """
        super().__init__(tag_name="tr", *tags, **props)


class Track(Element):
    """
    Represents the <track> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Track element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <track> tag.
            **props: Additional properties for the <track> tag.
        """
        super().__init__(tag_name="track", *tags, **props)


class U(Element):
    """
    Represents the <u> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the U element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <u> tag.
            **props: Additional properties for the <u> tag.
        """
        super().__init__(tag_name="u", *tags, **props)


class Ul(Element):
    """
    Represents the <ul> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Ul element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <ul> tag.
            **props: Additional properties for the <ul> tag.
        """
        super().__init__(tag_name="ul", *tags, **props)


class Var(Element):
    """
    Represents the <var> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Var element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <var> tag.
            **props: Additional properties for the <var> tag.
        """
        super().__init__(tag_name="var", *tags, **props)


class Video(Element):
    """
    Represents the <video> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Video element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <video> tag.
            **props: Additional properties for the <video> tag.
        """
        super().__init__(tag_name="video", *tags, **props)


class Wbr(Element):
    """
    Represents the <wbr> HTML element.
    """

    def __init__(
        self, *tags: Union[Iterable[str], Iterable[Element]], **props
    ):
        """
        Initialize the Wbr element.

        Args:
            *tags (str, Element): The list of tags to make content to be added to the <wbr> tag.
            **props: Additional properties for the <wbr> tag.
        """
        super().__init__(tag_name="wbr", *tags, **props)
