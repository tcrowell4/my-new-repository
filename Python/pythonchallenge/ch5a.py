import requests
from bs4 import BeautifulSoup, Comment
import re
import pickle
import urllib.request

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
    
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    raw_html = urllib.request.urlopen(url).read()
    print(pickle.loads(raw_html))
    #print(pickle.dumps(raw_html))
    data = pickle.load(urllib.request.urlopen(url))
    print(data)
    for line in data:
        print("".join([k * v for k, v in line]))


            
if __name__ == "__main__":
    main()
