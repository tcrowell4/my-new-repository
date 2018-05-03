
import requests
from bs4 import BeautifulSoup, Comment
import re
from PIL import Image
import urllib.request

"""
challenge 9

http://www.pythonchallenge.com/pc/return/good.html


"""
           
def main():
    
    """
    picture = Image.open("good.jpg")
    picture.show()
    print(picture.format)
    picture.close()
    """
    url = 'http://www.pythonchallenge.com/pc/return/5808.html'
    
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "http://www.pythonchallenge.com/pc/return/"
    password_mgr.add_password(None, top_level_url, "huge", "file")

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(url)

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)
    
    raw_html = urllib.request.urlopen(url).read()
    #print(pickle.loads(raw_html))
    print(raw_html)

    r = requests.get(url)
    r_html = r.text
    print(r_html)
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
