# HTML5 generator from your Python code

![GitHub Release](https://img.shields.io/github/v/release/old-juniors/markupify?include_prereleases&display_name=release&label=Release)
![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/old-juniors/markupify?query=is%3Aopen&label=Issues)
![PyPI - Downloads](https://img.shields.io/pypi/dm/markupify?label=Downloads)

# Features

- HTML5 tag creation with classes such as `A()` for `<a></a>`, `Hr()` for `<hr />`, etc.
- Pretty printing the html content with `pretty()` method.
- Create multiple html pages using `HTMLPage` class.
- Custom tag creation by inheriting `Element` class which declared at `markupify.tags`


# Goals

- Generate `*.html` files after creating html content.
- Create an `CSSPage` class to create some css contents.
- Generate `*.css` files.
- Show tag structure like `<body> -> <div> -> h1 -> "This is heading one!"` or something.
- Create a page object with specific head and body.


# Installation

```shell
pip install markupify
```


# Usage

```python
from markupify.page import HTMLPage
from markupify.tags import Meta, Link, Title, Div, H, Comment

# Alternatively, you can import these classes from markupify directly:
# from markupify import HTMLPage, Meta, Link, Title, Div, H, Comment


page = HTMLPage()

meta = Meta(charset="UTF-8")
link = Link(href="css/styles.css", rel="stylesheet")
title = Title("My first website")
div = Div(
    tag_content=H(
        tag_content="Greetings text"
    )
)
comment = Comment("This is a comment")

page.add_tag_to_head(meta, link, title)
page.add_tag_to_body(comment, div)

print(page)
```

Output:

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><link href="css/styles.css" rel="stylesheet" /><title>My first website</title></head><body><!-- This is a comment --><div><h1>Greetings text</h1></div></body></html>
```

To prettify that, use the `pretty()` method of the `page` object:

```python
print(page.pretty())
```

Output:

```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <link href="css/styles.css" rel="stylesheet"/>
  <title>
   My first website
  </title>
 </head>
 <body>
  <!-- This is a comment -->
  <div>
   <h1>
    Greetings text
   </h1>
  </div>
 </body>
</html>
```


# Customizing

> Devs! Maybe I forgot to create some tags you need. Feel free to create them yourself by inheriting from the `Element` class.

For example, create a double tag:

```python
from typing import Optional, Union
from markupify.tags import Element


class MyCustomTag(Element):
    def __init__(self, tag_content: Optional[Union[str, Element]], **props):
        """
        A tag class to represent <my_tag> tag.
        """
        super().__init__(tag_name="my_tag", tag_content=tag_content, **props)


my_tag = MyCustomTag("This my custom tag! 🥳")
print(my_tag)
```

Output:

```html
<my_tag>This my custom tag! 🥳</my_tag>
```

Add `class` property with `add_properties`

```python
my_tag.add_properties(_class="custom my-tag")
print(my_tag)
```

Output:

```html
<my_tag class="custom my-tag">This my custom tag! 🥳</my_tag>
```

> [!NOTE]
> Some keywords like `class` are built-in names in Python. So you need to use them with underscore before them.
> For example, instead of `class`, write `_class` and everything will be fine.


Create a single tag:

```python
from markupify.tags import Element


class Vl(Element):
    def __init__(self, **props):
        """
        A tag class to represent <vl> (Vertical Line) tag.
        """
        super().__init__(tag_name="vl", has_end_tag=False, **props)


vl = Vl()
print(vl)
```

Output:

```html
<vl />
```

Add `width` property with `add_property`

```python
vl.add_property("width", "5px")
print(vl)
```

Output:

```html
<vl width="5px" />
```
