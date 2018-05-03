import requests
from bs4 import BeautifulSoup
            
def main():
    
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    # loop through story headings and breakdown content
    #links = soup.find_all(class_="story-heading")
    for story in soup.find_all(class_="story-heading"):
        if story.a:
            print(story.a.text.replace("\n"," ").strip())
        else:
            print(story.contents[0].replace("\n"," ").strip())
            #print("story: ",story)
        #print("string: ",story.string)
        
        #print("story: ",story)
        #print()
    #print(s)
    
if __name__ == "__main__":
    main()
