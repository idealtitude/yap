-- Comments start wih a double dash
-- Programatic content generation within a code block
{% 
    -- Variable declaration
    $x = 4                        --literal integer
    $s = "Item "                  --literal string
    $list_of_items = %ul: .myul   -- yap tag declaration
    
    for $i in 1..$x:
        $list_of_items + %>li ($s $i) -- the + operator appends the li elements to the ul
        -- the > operator tells yap to indent the child
        -- the ^ operator would put it at the same level
        -- and < would dedent the element
        -- it produces then:
        -- ul: .myul
        --     li (Item 1)
        --     li (Item 2)
        -- etc.
        -- Then you can use that variable anywhere in your code
%}

!5 -- html5 doctype
html
    head
        meta: charset utf-8
        title (Page Title)
        meta: name viewport, content "width=device-width, initial-scale=1.0"
    body: class regular
        div: id global
            header: class myheader
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
                h2 (Welcome on my Website)
                {! <p>This a literal html element</p> !}
                hr
                -- insert the value of $list_of_items
                aside: #aside
                    $list_of_items
            footer: id footer
                $list_of_items -- insert the value of the variable here
            script: type module, src "./js/main.js"
            script ( −− Text node element, literal javascript
                const nav = document.querySelector(".navigation");
                // Do something with nav
            )
