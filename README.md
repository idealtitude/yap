# yap

**yap** stands for "Yet Another Preprocessor", and a HTML preprocessor in this case. **Important:** yap is under development, and not ready to use (I'll update this notice when it's ready to use).

## Presentation

I've choose that name as a funny reference to [Pug](https://pugjs.org/ "Pug Website"), as "yap" means something similar to "bark" in english, as a pug would do. By the way if you're a graphist and you'd like to contribute, the Yap project needs a logo, and I'd like it to simply be the contour of a pug barking, from the side view.

**yap* does not have strictly the same purpose as Pug, as it's not really a template engine, it only parse `.yap` files and produces HTML documents, also it's not a `node` package, it's a binary stand alone (with no dependencies, *a priori* (I don't know yet if I'll have to use some) written in C++.

## yap language

My goal from the start is to have a clean, easy to read, pretty, and clear content for yap files, so I've removed all that I can remove from standard html files, replacing them with significatives declaration (example: instead of writing tag's attributes like this `<a href="./page.html">`, in yap you just have `a: href ./page.html`), and to simplify the nesting of the DOM, it uses indentation: nested elements are indicated by indentation.
Also I intend to add a feature to programmatically generate contents (for example using variables, loops, conditional statement, even maybe `import`'s, etc.).

**Things to know:**

* comments start with a double dash `--`, they're ignored and can be at the start of any line, or at the end on any yap declaration line.
* nesting of elements is achieved through indentation:
* the tag name comes first; ex. `nav` rest of the declarations come after
* attributes list is declared by a colon `:`, each attribute is separated by a coma `,`, ex.: `a: href "some/page.html", title "This the title"
* as for any element, the text content of a tag is a `node`, it can be either written between parenthesis: `p (This is the content of the paragraph)`, or with an indented block, long strings or multiline string must be enclose between parenthesis.

**Important:** yap only supports HTML 5 markup!

Below is a basic example of a Yap file; **note:** to avoid ambiguity, the extension of Yap files is `.yaps` (for "yap source"), as the extensions `.yp`, `yap`, and other variants are already used for other purposes by other softwares.

```yaps
!5 -- doctype html 5, can be omiited for the moment as html 5 is the only supported version of html
html
    head
        meta: charset utf-8
        title (Page Title)
        meta: name viewport, content "width=device-width, initial-scale=1.0"
    body: class regular -- or .regular
        div: id global
            header: class myheader -- or #myheader
                h1: .myh1
                    span: .icon-home
                    a: title "Got to Home page", href ./index.html (My Website)
            nav: .navigation
                ul
                    li
                        a: href ./index.html (Home)
                    li
                        a: href ./about.html (About)
                    li
                        a: href ./contact.html (Contact)
            main: id main
            footer: id footer
            script: type "text/javaxscript", src "./js/main.js"
```

## Installation

**Prerequesites:** You're going to need `clang` (or `g++` (or any other C++ compiler that has C++23 support) if you prefer, but in that case you'll have to adapt the `Makefile`), and that's all.

Install steps:

* Download or clone this repository
* `cd yap`
* `make`

If anything went well, you'll now have a binary executable, that you move into a proper location (e.g. `/$HOME/bin` or `$HOME/.local/bin` (for a local "install", but you can also put it in `/usr/bin` to have it system wide, if you prefer) so that you have it your path, then you'll just have to do `yap my_yap_file.yap`.

## Usage

`yap -i file.yap -o output.html`

If no output is provided, `yap` will create a html file with the same name as the Yap file; also the input argument can be omiited for transpiling only one single Yap file. So the above command can be written like this `yap file.yap`.

For transpiling multiple files, it can be a good idea to use a Makefile, for ease of use and automation of the transpiling process.

## Contributing

If by any chance you're interested to contribute to this project, I'll be glad to have you in the team made of only one person, me. So please reach to me! :)
