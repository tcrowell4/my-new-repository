import requests
from bs4 import BeautifulSoup, Comment
import re

"""
challenge 5
"pronounce it"
http://www.pythonchallenge.com/pc/def/peak.html

answer:  peak hell sounds familiar ?
pickle?

http://www.pythonchallenge.com/pc/def/pickle.html
yes! pickle!


"""
           
def main():
    
    url = 'http://www.pythonchallenge.com/pc/def/peak.html'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    print(soup.prettify())
    for comments in soup.find_all(text=lambda text:isinstance(text, Comment)):
        print("Comments")
        print(comments)
        #print (x)
        #print(story.text.strip())

    """  keep around
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
