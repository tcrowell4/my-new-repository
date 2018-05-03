
import requests
from bs4 import BeautifulSoup, Comment
import re
from PIL import Image
import urllib.request
import pickle

"""
challenge 13 

http://www.pythonchallenge.com/pc/return/disproportional.html

"""
           
def main():
    
    """
    picture = Image.open("good.jpg")
    picture.show()
    print(picture.format)
    picture.close()
    """
    url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
    
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
    mystr = raw_html.decode('utf8')
    for line in mystr.split('\n'):
        print(line)


    return
    

            
if __name__ == "__main__":
    main()
