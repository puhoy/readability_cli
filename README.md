# readability_cli

a really small thing to fetch webpages main content and print it as markdown

basically its just [readability-lxml](https://github.com/buriy/python-readability) and [html2text](https://github.com/Alir3z4/html2text) glued together


## installation


    pip install git+https://github.com/puhoy/readability_cli --user


## usage 


    readcli SOMEURL

from there, you could pipe the result through [pygments](https://github.com/pygments/pygments) and a pager, for example:

    readcli https://github.com/puhoy/lspace | pygmentize -l md | less -R

or append website content to a file using vim:

    :read !readcli https://some/url

