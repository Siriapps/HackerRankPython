# https://www.hackerrank.com/challenges/html-parser-part-1/problem
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print("->",i[0],">",i[1])for i in attrs]

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print("->",i[0],">",i[1])for i in attrs]


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
