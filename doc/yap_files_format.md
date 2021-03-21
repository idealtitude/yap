# Yap files format

An example how to write a yap file can be found in test/doc.yap

Basically, yap files rely on indentation (for the moment the use of tabs (instead of spaces) is mandatory, in future version the user will have the choice to use whatever is prefered (tabs or spaces)); each line provides elements for the parser to create a representation of the html.

A line has to be written according to the following scheme:

[indention]<tag name>[:] [attributes] [~] [text content] [;]

Example:
```yap
p: href`page.html` .`myclass` title`My link title` ~ Text of the link
```
The above line compile to:

```html
<a href="page.html" class="myclass" title="My link title">
  Text of the link
</a>
```
