import requests
from bs4 import BeautifulSoup, Comment
import re

"""
main
Comments
linkedlist
Resulting URL redirects to linkedlist.php
http://www.pythonchallenge.com/pc/def/linkedlist.php

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
Follow the chainy

"""
           
def main():
    
    print("main")
    nextlink = '12345'
    # loop through story headings and breakdown content
    while True:
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' \
            % (nextlink)
        r = requests.get(url)
        r_html = r.text
        soup = BeautifulSoup(r_html, 'html.parser')
        for string in soup.stripped_strings:
            #print(repr(string))
            linked = repr(string)
        #print("\n****\n",linked)
        match = re.search(r'nothing is (\w+)', linked)
        if match:
            print("found %s  %s" % (match.group(1), linked))
            #url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % (match.group(1))
            nextlink = match.group(1)
        else:
            if linked.find('html') >= 0:
                # mystery found 'peak.html'
                print("mystery found", linked)
                break
            # 'Yes. Divide by two and keep going.'
            nextlink =  str(int(int(nextlink)/2))
            print(linked,nextlink)

    #print(soup.prettify())
    

    for tag in soup.find_all("body"):
        print(tag.name, tag.text)
        
        

            
if __name__ == "__main__":
    main()
