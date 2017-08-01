# Discussion
## Directly including Vue and bootstrap
Rather than use npm and a build system, I hand jammed the dependencies into my repository. I think this saved a sufficient amount of time and complexity to be worth it for this size project, but I would definitely want to change that for anything larger.
## Django-focused factoring
I ended up playing Django's game really hard with respect to serving files and creating html. This project could have been factored such that Django (or Flask) merely served a Rest API and the rest could have been constructed by Vue, which I'm guessing is a more modern pattern.
## Logging, tests, documentation
I swear I actually care about these things. These fell to the chopping block of time. Tests sometimes can improve time, but I don't know enough about testing in webapps to gain that speedup. There are docstrings in `models.py`, which might be the most important place.
## Interesting notes along the way
 -  Multiple github users with smart ssh
    <https://gist.github.com/jexchan/2351996>
