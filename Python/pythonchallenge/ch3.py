import requests
from bs4 import BeautifulSoup, Comment
import re

def find_rare(str):
    x = ""
    for char in str:
        if char.isalpha():
            x = x + char
    print("x = %s" % x)

def find_body_guard(str):
    bg  = re.compile(r"(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])")
    x = bg.findall(str)
    jewel = ""
    for char in x:
        jewel = jewel + char
    print(jewel)
            
def main():
    print("main")
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    # loop through story headings and breakdown content

    #print(soup.prettify())
    
    """
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    
    """

    for comments in soup.find_all(text=lambda text:isinstance(text, Comment)):
        print("Comments")
        #print(comments)
        find_body_guard(comments.extract())
        #print (x)
        #print(story.text.strip())
        
    """
    main
    Comments
    linkedlist
    Resulting URL redirects to linkedlist.php
    http://www.pythonchallenge.com/pc/def/linkedlist.php

    """
        

            
if __name__ == "__main__":
    main()
