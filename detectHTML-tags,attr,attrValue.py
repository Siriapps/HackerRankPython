#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]

text = ""
for _ in range(int(input())):
    parser = MyParser()
    text += input()
parser.feed(text)
