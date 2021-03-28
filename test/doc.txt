--- This a comment

!5
html: lang`fr`
	head
		meta: charset`utf-8` ;
		title ~ My title
		meta: name`viewport` content`width=device-width, initial-scale=1` ;
		link: rel`stylesheet` href`main.css` ;
	body
		div: #`page`
			header: #`header`
				h1: .`site-name` ~ My WebSite
				nav: #`nav`
					a: href`index.html` title`Home` ~ Accueil
					a: href`contact.html` title`Contact me` ~ Contact
					a: href`about.html` title`About` ~ A propos
			main: #`content`
				p ~ Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua.
				p ~ Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi utaliquip ex ea commodo consequat.
				br ;
				p ~ Duis aute irure dolor inreprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur.
				ul: .`main-ul`
					li ~ This is an item
					li ~ Another item
					li ~ Last item of the list
				p ~ Duis aute irure dolor inreprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur.
				p ~ Lorem ipsum dolor sit amet
			footer: #`footer`
				p
					a: .`icon-home footer-link` href`index.html` ~ Home
		script: src`main.js` ~
