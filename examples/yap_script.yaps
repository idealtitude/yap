{% 
-- function definition
$create_nav() =
    $myul = %ul: .myul
    for $i in 1..5:
        $myul + %>li %^a: href "./page$i.html", title "Page $i" (Page $i)
                -- the > operator tells yap to indent the element
                -- the ^ operator tells yap to keep the next element on the same line
                -- it could also be > to indent it on the next line   
export $create_nav
%}

-- You can use it in another document as it is exported
-- but to show how the function is called let's put it there:
-- At the beginning of a yap file let's do the import:
{% from scripts/utils import $create_nav as $cn %}

-- then later on in the document:
nav: .main_navgation
    $cn()
