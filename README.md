# readability_cli

a really small thing to fetch webpages main content and print it as markdown

basically its just [readability-lxml](https://github.com/buriy/python-readability) and [markdownify](https://github.com/matthewwithanm/python-markdownify) glued together


## installation


    pip install git+https://github.com/puhoy/readability_cli --user


## usage 


    readcli SOMEURL

from there, you could pipe the result through [pygments] and a pager, for example:

    readcli https://github.com/puhoy/lspace | pygmentize -l md | less -R

