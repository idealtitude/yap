# Yap files format

### Introduction

**Note:** An example how to write a yap file can be found in test/doc.yp

Basically, yap files rely on indentation (for the moment the use of tabs (instead of spaces) is mandatory, in future version the user will have the choice to use whatever is prefered (tabs or spaces)); each line provides elements for the parser to create a the final html source.

A line has to be written according to the following scheme:

```
[indention]<tag name>[:] [attributes] [~] [text content] [;]
```

**Important:** the yap files format is tabs and spaces sensitive, certain tokens require them for the transpiler to function properly. See for example the `;` in the scheme above, it indicates a self closing tag and the transpiler needs a space to know that it's not a part of text content (if any).

Example:

```yap
a: href`page.html` .`myclass` title`My link title` ~ Text of the link
```
The above line compile to:

```html
<a href="page.html" class="myclass" title="My link title">Text of the link</a>
```

----

## Basic rules

### Tags

#### Self closing tags

To indicate that the current line is a self closing tag, put a ` ;` at the end of the line (the space is mandatory).

#### Empty tags

To output an empty html element (e.g. `script tag`), a simple `~` at the end of the line is required; example:

```
script: src`main.js` ~
```

Transpiled to

```html
<script src="main.js"></script>
```

### Attributes

#### Booleans

Booleans attributes are defined with a `!` as their value; example:

```
input: required`!` type`text` ;
```

Transpiled to

```html
<input required type="text">
```

#### Empty values

TO add an attribute with empty value use a `?`; example:

```
img: alt`?` src`path/to/image.png`
```

Transpiled to

```html
<img alt="" src="path/to/image.png">
```

### Text content

Text content is indicated by a `~`, anything following this token will be considered as part of the string to form the text content of the element; example:

```
p ~ This is the text content of the element.
```

Transpiled to:

```html
<p>This is the text content of the element</p>
```

You can put other litteral html datas in the string (like `em`, `strong`, or whatever...), like so:

```
a: href`page.php` ~ This is the <em>text</em> content of the <strong>element</strong>
```

