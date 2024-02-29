class Element:
    """
    the base class to make an HTML element.

    Args:
        tag_name (str) - The tag name.
        has_end_tag (bool, Optional) - If set to False, the tag will not contain content and end tag. Default: True.
        props - Properties for the tag.
    """

    def __init__(
            self,
            tag_name: str = "div",
            has_end_tag: bool = True,
            tag_content: str = "",
            **props: object
    ) -> None:
        if not has_end_tag and tag_content:
            raise ValueError("Tags without end parts cannot contain content. "
                             "Set has_end_tag to True or leave blank the tag_content.")

        self.tag_name = tag_name.lower()
        self.has_end_tag = has_end_tag
        self.tag_content = tag_content
        self.props = ""
        self.style = ""

        style_property = props.pop("style")
        if style_property:
            if isinstance(style_property, str):
                self.style += style_property
            elif isinstance(style_property, dict):
                self.add_styles(**style_property)
            else:
                raise TypeError("style property must be string or dict.")

        props["style"] = self.style
        self.add_properties(**props)

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        structure = "<{tag_name}"

        if self.props:
            structure += " {props}"
        structure += ">"
        if self.tag_content:
            structure += "{tag_content}"

        if self.has_end_tag:
            structure += "</{tag_name}>"
        elif not self.has_end_tag:
            structure += " />"

        return structure.format(
            tag_name=self.tag_name,
            props=self.props,
            tag_content=self.tag_content,
        )

    def add_property(self, name: str, value: str) -> None:
        self.props += f'{name}="{value}"'

    def add_properties(self, **props) -> None:
        for name, value in props.items():
            name = name.replace("_", "-")
            self.add_property(name, value)

    def add_style(self, name: str, value: str) -> None:
        self.style += f"{name}: {value};"

    def add_styles(self, **styles):
        for name, value in styles.items():
            name = name.replace("_", "-")
            self.add_style(name, value)


class A(Element):
    def __init__(self, link: str, tag_content: str = "", **props):
        super().__init__(tag_name="a", tag_content=tag_content, href=link, **props)


class Abbr(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="abbr", tag_content=tag_content, **props)


class Address(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="address", tag_content=tag_content, **props)


class Area(Element):
    def __init__(self, **props):
        super().__init__(tag_name="area", has_end_tag=False, **props)


class Article(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="article", tag_content=tag_content, **props)


class Aside(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="aside", tag_content=tag_content, **props)


class Audio(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="audio", tag_content=tag_content, **props)


class B(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="b", tag_content=tag_content, **props)


class Base(Element):
    def __init__(self, **props):
        super().__init__(tag_name="base", has_end_tag=False, **props)


class Bdi(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="bdi", tag_content=tag_content, **props)


class Bdo(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="bdo", tag_content=tag_content, **props)


class BlockQuote(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="blockquote", tag_content=tag_content, **props)


class Body(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="body", tag_content=tag_content, **props)


class Br(Element):
    def __init__(self):
        super().__init__(tag_name="br", has_end_tag=False)


class Button(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="button", tag_content=tag_content, **props)


class Canvas(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="canvas", tag_content=tag_content, **props)


class Caption(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="caption", tag_content=tag_content, **props)


class Circle(Element):
    def __init__(self, **props):
        super().__init__(tag_content="circle", has_end_tag=False, **props)


class Cite(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="cite", tag_content=tag_content, **props)


class Code(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="code", tag_content=tag_content, **props)


class Col(Element):
    def __init__(self, **props):
        super().__init__(tag_content="col", has_end_tag=False, **props)


class ColGroup(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="colgroup", tag_content=tag_content, **props)


class Comment:
    def __init__(self, tag_content: str = "", multiline: bool = False):
        self.tag_content = tag_content
        self.multiline = multiline

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()

    def render(self) -> str:
        if self.multiline:
            return f"""
            <!--
                {self.tag_content}
            -->
            """.strip()
        return f"<!-- {self.tag_content} -->"


class Data(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="data", tag_content=tag_content, **props)


class DataList(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="datalist", tag_content=tag_content, **props)


class Dd(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="dd", tag_content=tag_content, **props)


class Defs(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="defs", tag_content=tag_content, **props)


class Del(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="del", tag_content=tag_content, **props)


class Details(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="details", tag_content=tag_content, **props)


class Dfn(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="dfn", tag_content=tag_content, **props)


class Dialog(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="dialog", tag_content=tag_content, **props)


class Div(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="div", tag_content=tag_content, **props)


class Dl(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="dl", tag_content=tag_content, **props)


class DocType:
    def __init__(self, doc_type: str = "html"):
        self.doc_type = doc_type

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()

    def render(self) -> str:
        return f"<!DOCTYPE {self.doc_type}>"


class Dt(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="dt", tag_content=tag_content, **props)


class Ellipse(Element):
    def __init__(self, **props):
        super().__init__(tag_name="ellipse", has_end_tag=False, **props)


class Em(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="em", tag_content=tag_content, **props)


class Embed(Element):
    def __init__(self, **props):
        super().__init__(tag_name="embed", has_end_tag=False, **props)


class FieldSet(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="fieldset", tag_content=tag_content, **props)


class FigCaption(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="figcaption", tag_content=tag_content, **props)


class Figure(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="figure", tag_content=tag_content, **props)


class Footer(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="footer", tag_content=tag_content, **props)


class Form(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="form", tag_content=tag_content, **props)


class H(Element):
    def __init__(self, level: int = 1, tag_content: str = "", **props):
        if not 1 < level < 6:
            raise ValueError("The heading level must be an integer in range 1-6.")
        super().__init__(tag_name=f"h{level}", tag_content=tag_content, **props)


class Head(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="head", tag_content=tag_content, **props)


class Header(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="header", tag_content=tag_content, **props)


class HGroup(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="hgroup", tag_content=tag_content, **props)


class Hr(Element):
    def __init__(self):
        super().__init__(tag_name="hr", has_end_tag=False)


class Html(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="html", tag_content=tag_content, **props)


class I(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="i", tag_content=tag_content, **props)


class IFrame(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="iframe", tag_content=tag_content, **props)


class Img(Element):
    def __init__(self, src: str, **props):
        super().__init__(tag_name="img", has_end_tag=False, src=src, **props)


class Input(Element):
    def __init__(self, **props):
        super().__init__(tag_name="input", has_end_tag=False, **props)


class Ins(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="ins", tag_content=tag_content, **props)


class Kbd(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="kbd", tag_content=tag_content, **props)


class Label(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="label", tag_content=tag_content, **props)


class Legend(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="legend", tag_content=tag_content, **props)


class Li(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="li", tag_content=tag_content, **props)


class LinearGradient(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="linearGradient", tag_content=tag_content, **props)


class Link(Element):
    def __init__(self, **props):
        super().__init__(tag_name="link", has_end_tag=False, **props)


class Main(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="main", tag_content=tag_content, **props)


class Map(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="map", tag_content=tag_content, **props)


class Mark(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="mark", tag_content=tag_content, **props)


class Menu(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="menu", tag_content=tag_content, **props)


class Meta(Element):
    def __init__(self, **props):
        super().__init__(tag_name="meta", has_end_tag=False, **props)


class Meter(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="meter", tag_content=tag_content, **props)


class Nav(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="nav", tag_content=tag_content, **props)


class NoScript(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="noscript", tag_content=tag_content, **props)


class Object(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="option", tag_content=tag_content, **props)


class Ol(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="ol", tag_content=tag_content, **props)


class OptGroup(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="optgroup", tag_content=tag_content, **props)


class Option(Element):
    def __init__(self, tag_content: str, **props):
        super().__init__(tag_name="option", tag_content=tag_content, **props)


class Output(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="output", tag_content=tag_content, **props)


class P(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="p", tag_content=tag_content, **props)


class Param(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="param", tag_content=tag_content, **props)


class Picture(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="picture", tag_content=tag_content, **props)


class Polygon(Element):
    def __init__(self, **props):
        super().__init__(tag_name="polygon", has_end_tag=False, **props)


class Pre(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="pre", tag_content=tag_content, **props)


class Progress(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="progress", tag_content=tag_content, **props)


class Q(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="q", tag_content=tag_content, **props)


class Rect(Element):
    def __init__(self, **props):
        super().__init__(tag_name="rect", has_end_tag=False, **props)


class Rp(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="rp", tag_content=tag_content, **props)


class Rt(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="rt", tag_content=tag_content, **props)


class Ruby(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="ruby", tag_content=tag_content, **props)


class S(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="s", tag_content=tag_content, **props)


class Samp(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="samp", tag_content=tag_content, **props)


class Script(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="script", tag_content=tag_content, **props)


class Search(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="search", tag_content=tag_content, **props)


class Section(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="section", tag_content=tag_content, **props)


class Select(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="select", tag_content=tag_content, **props)


class Small(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="small", tag_content=tag_content, **props)


class Source(Element):
    def __init__(self, **props):
        super().__init__(tag_name="source", has_end_tag=False, **props)


class Span(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="span", tag_content=tag_content, **props)


class Stop(Element):
    def __init__(self, **props):
        super().__init__(tag_name="stop", has_end_tag=False, **props)


class Strong(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="strong", tag_content=tag_content, **props)


class Style(Element):
    def __init__(self, **props):
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
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="sub", tag_content=tag_content, **props)


class Summary(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="summary", tag_content=tag_content, **props)


class Sup(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="sup", tag_content=tag_content, **props)


class Svg(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="svg", tag_content=tag_content, **props)


class Table(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="table", tag_content=tag_content, **props)


class TBody(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="tbody", tag_content=tag_content, **props)


class Td(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="td", tag_content=tag_content, **props)


class Template(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="template", tag_content=tag_content, **props)


class Text(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="text", tag_content=tag_content, **props)


class Textarea(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="textarea", tag_content=tag_content, **props)


class TFoot(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="tfoot", tag_content=tag_content, **props)


class Th(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="th", tag_content=tag_content, **props)


class THead(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="thead", tag_content=tag_content, **props)


class Time(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="time", tag_content=tag_content, **props)


class Title(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="title", tag_content=tag_content, **props)


class Tr(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="tr", tag_content=tag_content, **props)


class Track(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="track", tag_content=tag_content, **props)


class U(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="u", tag_content=tag_content, **props)


class Ul(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="ul", tag_content=tag_content, **props)


class Var(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="var", tag_content=tag_content, **props)


class Video(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="video", tag_content=tag_content, **props)


class Wbr(Element):
    def __init__(self, tag_content: str = "", **props):
        super().__init__(tag_name="wbr", tag_content=tag_content, **props)
