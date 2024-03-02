from typing import Optional, Any, Union


class Element:
    """
    The base class to make an HTML element.

    Args:
        tag_name (str): The tag name.
        has_end_tag (bool, optional): If set to False, the tag will not contain content and end tag. Default: True.
        tag_content (str or Element, optional): The content of the tag.
        **props: Properties for the tag.

    Attributes:
        tag_name (str): The tag name.
        has_end_tag (bool): Indicates whether the tag has an end tag.
        tag_content (str or Element): The content of the tag.
        properties (dict): Properties for the tag.
        props (str): String representation of the tag properties.
        style (str): CSS style string.

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
            tag_content: Optional[str] = "",
            **props: object
    ) -> None:
        """
        Initialize the Element instance.

        Args:
            tag_name (str, optional): The tag name. Defaults to "div".
            has_end_tag (bool, optional): If set to False, the tag will not contain content and end tag. Default: True.
            tag_content (str or Element, optional): The content of the tag. Defaults to "".
            **props: Properties for the tag.
        """
        if not has_end_tag and tag_content:
            raise ValueError("Tags without end parts cannot contain content. "
                             "Set has_end_tag to True or leave blank the tag_content.")

        self.tag_name = tag_name.lower()
        self.has_end_tag = has_end_tag
        self.tag_content = tag_content
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
            self.properties["style"] = self.style
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

    def __add__(self, other: Union[str, 'Element']) -> 'Element':
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
            **self.properties
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
            name = name.replace("_", "-")
            self.add_style(name, value)

    def add_content(self, tag_content: Union[str, 'Element']) -> None:
        """
        Add content to the tag.

        Args:
            tag_content (str, Element): The content to be added to the tag.
        """
        self.tag_content += tag_content

    @property
    def text(self) -> [str, 'Element']:
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
    def __init__(self, link: str, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the A element.

        Args:
            link (str): The URL the hyperlink points to.
            tag_content (Optional, str or Element): The content of the <a> tag.
            **props: Additional properties for the <a> tag.
        """
        super().__init__(tag_name="a", tag_content=tag_content, href=link, **props)


class Abbr(Element):
    """
    Represents the <abbr> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Abbr element.

        Args:
            tag_content (Optional[Union[str, 'Element']]git status): The content of the <abbr> tag.
            **props: Additional properties for the <abbr> tag.
        """
        super().__init__(tag_name="abbr", tag_content=tag_content, **props)


class Address(Element):
    """
    Represents the <address> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Address element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <address> tag.
            **props: Additional properties for the <address> tag.
        """
        super().__init__(tag_name="address", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Article element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <article> tag.
            **props: Additional properties for the <article> tag.
        """
        super().__init__(tag_name="article", tag_content=tag_content, **props)


class Aside(Element):
    """
    Represents the <aside> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Aside element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <aside> tag.
            **props: Additional properties for the <aside> tag.
        """
        super().__init__(tag_name="aside", tag_content=tag_content, **props)


class Audio(Element):
    """
    Represents the <audio> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Audio element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <audio> tag.
            **props: Additional properties for the <audio> tag.
        """
        super().__init__(tag_name="audio", tag_content=tag_content, **props)


class B(Element):
    """
    Represents the <b> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the B element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <b> tag.
            **props: Additional properties for the <b> tag.
        """
        super().__init__(tag_name="b", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Bdi element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <bdi> tag.
            **props: Additional properties for the <bdi> tag.
        """
        super().__init__(tag_name="bdi", tag_content=tag_content, **props)


class Bdo(Element):
    """
    Represents the <bdo> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Bdo element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <bdo> tag.
            **props: Additional properties for the <bdo> tag.
        """
        super().__init__(tag_name="bdo", tag_content=tag_content, **props)


class BlockQuote(Element):
    """
    Represents the <blockquote> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the BlockQuote element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <blockquote> tag.
            **props: Additional properties for the <blockquote> tag.
        """
        super().__init__(tag_name="blockquote", tag_content=tag_content, **props)


class Body(Element):
    """
    Represents the <body> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Body element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <body> tag.
            **props: Additional properties for the <body> tag.
        """
        super().__init__(tag_name="body", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Button element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <button> tag.
            **props: Additional properties for the <button> tag.
        """
        super().__init__(tag_name="button", tag_content=tag_content, **props)


class Canvas(Element):
    """
    Represents the <canvas> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Canvas element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <canvas> tag.
            **props: Additional properties for the <canvas> tag.
        """
        super().__init__(tag_name="canvas", tag_content=tag_content, **props)


class Caption(Element):
    """
    Represents the <caption> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Caption element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <caption> tag.
            **props: Additional properties for the <caption> tag.
        """
        super().__init__(tag_name="caption", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Cite element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <cite> tag.
            **props: Additional properties for the <cite> tag.
        """
        super().__init__(tag_name="cite", tag_content=tag_content, **props)


class Code(Element):
    """
    Represents the <code> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Code element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <code> tag.
            **props: Additional properties for the <code> tag.
        """
        super().__init__(tag_name="code", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the ColGroup element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <colgroup> tag.
            **props: Additional properties for the <colgroup> tag.
        """
        super().__init__(tag_name="colgroup", tag_content=tag_content, **props)


class Comment:
    """
    Represents an HTML comment.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", multiline: bool = False):
        """
        Initialize the Comment.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the comment.
            multiline (bool): Indicates if the comment spans multiple lines.
        """
        self.tag_content = tag_content
        self.multiline = multiline

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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Data element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <data> tag.
            **props: Additional properties for the <data> tag.
        """
        super().__init__(tag_name="data", tag_content=tag_content, **props)


class DataList(Element):
    """
    Represents the <datalist> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the DataList element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <datalist> tag.
            **props: Additional properties for the <datalist> tag.
        """
        super().__init__(tag_name="datalist", tag_content=tag_content, **props)


class Dd(Element):
    """
    Represents the <dd> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Dd element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <dd> tag.
            **props: Additional properties for the <dd> tag.
        """
        super().__init__(tag_name="dd", tag_content=tag_content, **props)


class Defs(Element):
    """
    Represents the <defs> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Defs element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <defs> tag.
            **props: Additional properties for the <defs> tag.
        """
        super().__init__(tag_name="defs", tag_content=tag_content, **props)


class Del(Element):
    """
    Represents the <del> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Del element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <del> tag.
            **props: Additional properties for the <del> tag.
        """
        super().__init__(tag_name="del", tag_content=tag_content, **props)


class Details(Element):
    """
    Represents the <details> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Details element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <details> tag.
            **props: Additional properties for the <details> tag.
        """
        super().__init__(tag_name="details", tag_content=tag_content, **props)


class Dfn(Element):
    """
    Represents the <dfn> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Dfn element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <dfn> tag.
            **props: Additional properties for the <dfn> tag.
        """
        super().__init__(tag_name="dfn", tag_content=tag_content, **props)


class Dialog(Element):
    """
    Represents the <dialog> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Dialog element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <dialog> tag.
            **props: Additional properties for the <dialog> tag.
        """
        super().__init__(tag_name="dialog", tag_content=tag_content, **props)


class Div(Element):
    """
    Represents the <div> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Div element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <div> tag.
            **props: Additional properties for the <div> tag.
        """
        super().__init__(tag_name="div", tag_content=tag_content, **props)


class Dl(Element):
    """
    Represents the <dl> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Dl element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <dl> tag.
            **props: Additional properties for the <dl> tag.
        """
        super().__init__(tag_name="dl", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Dt element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <dt> tag.
            **props: Additional properties for the <dt> tag.
        """
        super().__init__(tag_name="dt", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Em element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <em> tag.
            **props: Additional properties for the <em> tag.
        """
        super().__init__(tag_name="em", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the FieldSet element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <fieldset> tag.
            **props: Additional properties for the <fieldset> tag.
        """
        super().__init__(tag_name="fieldset", tag_content=tag_content, **props)


class FigCaption(Element):
    """
    Represents the <figcaption> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the FigCaption element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <figcaption> tag.
            **props: Additional properties for the <figcaption> tag.
        """
        super().__init__(tag_name="figcaption", tag_content=tag_content, **props)


class Figure(Element):
    """
    Represents the <figure> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Figure element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <figure> tag.
            **props: Additional properties for the <figure> tag.
        """
        super().__init__(tag_name="figure", tag_content=tag_content, **props)


class Footer(Element):
    """
    Represents the <footer> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Footer element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <footer> tag.
            **props: Additional properties for the <footer> tag.
        """
        super().__init__(tag_name="footer", tag_content=tag_content, **props)


class Form(Element):
    """
    Represents the <form> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Form element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <form> tag.
            **props: Additional properties for the <form> tag.
        """
        super().__init__(tag_name="form", tag_content=tag_content, **props)


class H(Element):
    """
    Represents a heading (h1 - h6) HTML element.
    """
    def __init__(self, level: int = 1, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the H element.

        Args:
            level (int): The level of the heading (1-6).
            tag_content (Optional[Union[str, 'Element']]): The content of the heading tag.
            **props: Additional properties for the heading tag.
        """
        if not 1 <= level <= 6:
            raise ValueError("The heading level must be an integer in range 1-6.")
        super().__init__(tag_name=f"h{level}", tag_content=tag_content, **props)


class Head(Element):
    """
    Represents the <head> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Head element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <head> tag.
            **props: Additional properties for the <head> tag.
        """
        super().__init__(tag_name="head", tag_content=tag_content, **props)


class Header(Element):
    """
    Represents the <header> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Header element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <header> tag.
            **props: Additional properties for the <header> tag.
        """
        super().__init__(tag_name="header", tag_content=tag_content, **props)


class HGroup(Element):
    """
    Represents the <hgroup> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the HGroup element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <hgroup> tag.
            **props: Additional properties for the <hgroup> tag.
        """
        super().__init__(tag_name="hgroup", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Html element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <html> tag.
            **props: Additional properties for the <html> tag.
        """
        super().__init__(tag_name="html", tag_content=tag_content, **props)


class I(Element):
    """
    Represents the <i> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the I element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <i> tag.
            **props: Additional properties for the <i> tag.
        """
        super().__init__(tag_name="i", tag_content=tag_content, **props)


class IFrame(Element):
    """
    Represents the <iframe> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the IFrame element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <iframe> tag.
            **props: Additional properties for the <iframe> tag.
        """
        super().__init__(tag_name="iframe", tag_content=tag_content, **props)


class Img(Element):
    """
    Represents the <img> HTML element.
    """
    def __init__(self, src: str, **props):
        """
        Initialize the Img element.

        Args:
            src (str): The source URL of the image.
            **props: Additional properties for the <img> tag.
        """
        super().__init__(tag_name="img", has_end_tag=False, src=src, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Ins element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <ins> tag.
            **props: Additional properties for the <ins> tag.
        """
        super().__init__(tag_name="ins", tag_content=tag_content, **props)


class Kbd(Element):
    """
    Represents the <kbd> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Kbd element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <kbd> tag.
            **props: Additional properties for the <kbd> tag.
        """
        super().__init__(tag_name="kbd", tag_content=tag_content, **props)


class Label(Element):
    """
    Represents the <label> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Label element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <label> tag.
            **props: Additional properties for the <label> tag.
        """
        super().__init__(tag_name="label", tag_content=tag_content, **props)


class Legend(Element):
    """
    Represents the <legend> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Legend element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <legend> tag.
            **props: Additional properties for the <legend> tag.
        """
        super().__init__(tag_name="legend", tag_content=tag_content, **props)


class Li(Element):
    """
    Represents the <li> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Li element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <li> tag.
            **props: Additional properties for the <li> tag.
        """
        super().__init__(tag_name="li", tag_content=tag_content, **props)


class LinearGradient(Element):
    """
    Represents the <linearGradient> SVG element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the LinearGradient element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <linearGradient> tag.
            **props: Additional properties for the <linearGradient> tag.
        """
        super().__init__(tag_name="linearGradient", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Main element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <main> tag.
            **props: Additional properties for the <main> tag.
        """
        super().__init__(tag_name="main", tag_content=tag_content, **props)


class Map(Element):
    """
    Represents the <map> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Map element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <map> tag.
            **props: Additional properties for the <map> tag.
        """
        super().__init__(tag_name="map", tag_content=tag_content, **props)


class Mark(Element):
    """
    Represents the <mark> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Mark element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <mark> tag.
            **props: Additional properties for the <mark> tag.
        """
        super().__init__(tag_name="mark", tag_content=tag_content, **props)


class Menu(Element):
    """
    Represents the <menu> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Menu element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <menu> tag.
            **props: Additional properties for the <menu> tag.
        """
        super().__init__(tag_name="menu", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Meter element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <meter> tag.
            **props: Additional properties for the <meter> tag.
        """
        super().__init__(tag_name="meter", tag_content=tag_content, **props)


class Nav(Element):
    """
    Represents the <nav> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Nav element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <nav> tag.
            **props: Additional properties for the <nav> tag.
        """
        super().__init__(tag_name="nav", tag_content=tag_content, **props)


class NoScript(Element):
    """
    Represents the <noscript> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the NoScript element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <noscript> tag.
            **props: Additional properties for the <noscript> tag.
        """
        super().__init__(tag_name="noscript", tag_content=tag_content, **props)


class Object(Element):
    """
    Represents the <object> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Object element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <object> tag.
            **props: Additional properties for the <object> tag.
        """
        super().__init__(tag_name="option", tag_content=tag_content, **props)


class Ol(Element):
    """
    Represents the <ol> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Ol element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <ol> tag.
            **props: Additional properties for the <ol> tag.
        """
        super().__init__(tag_name="ol", tag_content=tag_content, **props)


class OptGroup(Element):
    """
    Represents the <optgroup> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the OptGroup element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <optgroup> tag.
            **props: Additional properties for the <optgroup> tag.
        """
        super().__init__(tag_name="optgroup", tag_content=tag_content, **props)


class Option(Element):
    """
    Represents the <option> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']], **props):
        """
        Initialize the Option element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <option> tag.
            **props: Additional properties for the <option> tag.
        """
        super().__init__(tag_name="option", tag_content=tag_content, **props)


class Output(Element):
    """
    Represents the <output> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Output element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <output> tag.
            **props: Additional properties for the <output> tag.
        """
        super().__init__(tag_name="output", tag_content=tag_content, **props)


class P(Element):
    """
    Represents the <p> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the P element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <p> tag.
            **props: Additional properties for the <p> tag.
        """
        super().__init__(tag_name="p", tag_content=tag_content, **props)


class Param(Element):
    """
    Represents the <param> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Param element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <param> tag.
            **props: Additional properties for the <param> tag.
        """
        super().__init__(tag_name="param", tag_content=tag_content, **props)


class Picture(Element):
    """
    Represents the <picture> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Picture element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <picture> tag.
            **props: Additional properties for the <picture> tag.
        """
        super().__init__(tag_name="picture", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Pre element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <pre> tag.
            **props: Additional properties for the <pre> tag.
        """
        super().__init__(tag_name="pre", tag_content=tag_content, **props)


class Progress(Element):
    """
    Represents the <progress> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Progress element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <progress> tag.
            **props: Additional properties for the <progress> tag.
        """
        super().__init__(tag_name="progress", tag_content=tag_content, **props)


class Q(Element):
    """
    Represents the <q> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Q element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <q> tag.
            **props: Additional properties for the <q> tag.
        """
        super().__init__(tag_name="q", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Rp element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <rp> tag.
            **props: Additional properties for the <rp> tag.
        """
        super().__init__(tag_name="rp", tag_content=tag_content, **props)


class Rt(Element):
    """
    Represents the <rt> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Rt element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <rt> tag.
            **props: Additional properties for the <rt> tag.
        """
        super().__init__(tag_name="rt", tag_content=tag_content, **props)


class Ruby(Element):
    """
    Represents the <ruby> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Ruby element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <ruby> tag.
            **props: Additional properties for the <ruby> tag.
        """
        super().__init__(tag_name="ruby", tag_content=tag_content, **props)


class S(Element):
    """
    Represents the <s> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the S element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <s> tag.
            **props: Additional properties for the <s> tag.
        """
        super().__init__(tag_name="s", tag_content=tag_content, **props)


class Samp(Element):
    """
    Represents the <samp> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Samp element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <samp> tag.
            **props: Additional properties for the <samp> tag.
        """
        super().__init__(tag_name="samp", tag_content=tag_content, **props)


class Script(Element):
    """
    Represents the <script> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Script element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <script> tag.
            **props: Additional properties for the <script> tag.
        """
        super().__init__(tag_name="script", tag_content=tag_content, **props)


class Search(Element):
    """
    Represents the <search> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Search element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <search> tag.
            **props: Additional properties for the <search> tag.
        """
        super().__init__(tag_name="search", tag_content=tag_content, **props)


class Section(Element):
    """
    Represents the <section> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Section element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <section> tag.
            **props: Additional properties for the <section> tag.
        """
        super().__init__(tag_name="section", tag_content=tag_content, **props)


class Select(Element):
    """
    Represents the <select> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Select element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <select> tag.
            **props: Additional properties for the <select> tag.
        """
        super().__init__(tag_name="select", tag_content=tag_content, **props)


class Small(Element):
    """
    Represents the <small> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Small element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <small> tag.
            **props: Additional properties for the <small> tag.
        """
        super().__init__(tag_name="small", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Span element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <span> tag.
            **props: Additional properties for the <span> tag.
        """
        super().__init__(tag_name="span", tag_content=tag_content, **props)


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
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Strong element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <strong> tag.
            **props: Additional properties for the <strong> tag.
        """
        super().__init__(tag_name="strong", tag_content=tag_content, **props)


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
                val = "".join(f"{k.replace('_', '-')}: {v};" for k, v in value.items())
                tag_content += f"{key} {val}"
            elif isinstance(value, str):
                tag_content += f"{key} {value}"

            else:
                raise TypeError("property must be string or dict.")
        super().__init__(tag_name="style", tag_content=tag_content, **props)


class Sub(Element):
    """
    Represents the <sub> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Sub element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <sub> tag.
            **props: Additional properties for the <sub> tag.
        """
        super().__init__(tag_name="sub", tag_content=tag_content, **props)


class Summary(Element):
    """
    Represents the <summary> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Summary element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <summary> tag.
            **props: Additional properties for the <summary> tag.
        """
        super().__init__(tag_name="summary", tag_content=tag_content, **props)


class Sup(Element):
    """
    Represents the <sup> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Sup element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <sup> tag.
            **props: Additional properties for the <sup> tag.
        """
        super().__init__(tag_name="sup", tag_content=tag_content, **props)


class Svg(Element):
    """
    Represents the <svg> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Svg element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <svg> tag.
            **props: Additional properties for the <svg> tag.
        """
        super().__init__(tag_name="svg", tag_content=tag_content, **props)


class Table(Element):
    """
    Represents the <table> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Table element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <table> tag.
            **props: Additional properties for the <table> tag.
        """
        super().__init__(tag_name="table", tag_content=tag_content, **props)


class TBody(Element):
    """
    Represents the <tbody> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the TBody element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <tbody> tag.
            **props: Additional properties for the <tbody> tag.
        """
        super().__init__(tag_name="tbody", tag_content=tag_content, **props)


class Td(Element):
    """
    Represents the <td> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Td element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <td> tag.
            **props: Additional properties for the <td> tag.
        """
        super().__init__(tag_name="td", tag_content=tag_content, **props)


class Template(Element):
    """
    Represents the <template> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Template element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <template> tag.
            **props: Additional properties for the <template> tag.
        """
        super().__init__(tag_name="template", tag_content=tag_content, **props)


class Text(Element):
    """
    Represents the <text> SVG element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Text element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <text> tag.
            **props: Additional properties for the <text> tag.
        """
        super().__init__(tag_name="text", tag_content=tag_content, **props)


class Textarea(Element):
    """
    Represents the <textarea> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Textarea element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <textarea> tag.
            **props: Additional properties for the <textarea> tag.
        """
        super().__init__(tag_name="textarea", tag_content=tag_content, **props)


class TFoot(Element):
    """
    Represents the <tfoot> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the TFoot element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <tfoot> tag.
            **props: Additional properties for the <tfoot> tag.
        """
        super().__init__(tag_name="tfoot", tag_content=tag_content, **props)


class Th(Element):
    """
    Represents the <th> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Th element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <th> tag.
            **props: Additional properties for the <th> tag.
        """
        super().__init__(tag_name="th", tag_content=tag_content, **props)


class THead(Element):
    """
    Represents the <thead> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the THead element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <thead> tag.
            **props: Additional properties for the <thead> tag.
        """
        super().__init__(tag_name="thead", tag_content=tag_content, **props)


class Time(Element):
    """
    Represents the <time> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Time element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <time> tag.
            **props: Additional properties for the <time> tag.
        """
        super().__init__(tag_name="time", tag_content=tag_content, **props)


class Title(Element):
    """
    Represents the <title> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Title element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <title> tag.
            **props: Additional properties for the <title> tag.
        """
        super().__init__(tag_name="title", tag_content=tag_content, **props)


class Tr(Element):
    """
    Represents the <tr> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Tr element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <tr> tag.
            **props: Additional properties for the <tr> tag.
        """
        super().__init__(tag_name="tr", tag_content=tag_content, **props)


class Track(Element):
    """
    Represents the <track> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Track element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <track> tag.
            **props: Additional properties for the <track> tag.
        """
        super().__init__(tag_name="track", tag_content=tag_content, **props)


class U(Element):
    """
    Represents the <u> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the U element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <u> tag.
            **props: Additional properties for the <u> tag.
        """
        super().__init__(tag_name="u", tag_content=tag_content, **props)


class Ul(Element):
    """
    Represents the <ul> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Ul element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <ul> tag.
            **props: Additional properties for the <ul> tag.
        """
        super().__init__(tag_name="ul", tag_content=tag_content, **props)


class Var(Element):
    """
    Represents the <var> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Var element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <var> tag.
            **props: Additional properties for the <var> tag.
        """
        super().__init__(tag_name="var", tag_content=tag_content, **props)


class Video(Element):
    """
    Represents the <video> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Video element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <video> tag.
            **props: Additional properties for the <video> tag.
        """
        super().__init__(tag_name="video", tag_content=tag_content, **props)


class Wbr(Element):
    """
    Represents the <wbr> HTML element.
    """
    def __init__(self, tag_content: Optional[Union[str, 'Element']] = "", **props):
        """
        Initialize the Wbr element.

        Args:
            tag_content (Optional[Union[str, 'Element']]): The content of the <wbr> tag.
            **props: Additional properties for the <wbr> tag.
        """
        super().__init__(tag_name="wbr", tag_content=tag_content, **props)
