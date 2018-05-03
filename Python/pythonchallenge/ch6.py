import requests
from bs4 import BeautifulSoup, Comment
import re
import pickle
import urllib.request

"""
challenge 6
now there are pairs    
http://www.pythonchallenge.com/pc/def/channel.html

 <!-- <-- zip -->


"""
           
def main():
    
    url = 'http://www.pythonchallenge.com/pc/def/channel.html'
    raw_html = urllib.request.urlopen(url).read()
    #print(pickle.loads(raw_html))

    r = requests.get(url)
    r_html = r.text
    #print(r_html)
    soup = BeautifulSoup(r_html, 'html.parser')
    print(soup.prettify())

    """  keep around
    for comments in soup.find_all(text=lambda text:isinstance(text, Comment)):
        print("Comments")
        print(comments)
        #print (x)
        #print(story.text.strip())
    for string in soup.stripped_strings:
        #print(repr(string))
        linked = repr(string)
        print("\n****\n",linked)
    print(soup.prettify())
    

    for tag in soup.find_all("body"):
        print(tag.name, tag.text)
        
    """

            
if __name__ == "__main__":
    main()
