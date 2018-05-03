import requests
from bs4 import BeautifulSoup
            
def main():
    
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    # loop through story headings and breakdown content

    with open('ex21_write_a_file.txt', 'w') as open_file:
        for story in soup.find_all(class_="story-heading"):
            if story.a:
                story_line = story.a.text.replace("\n"," ").strip()
                #print(story.a.text.replace("\n"," ").strip())
            else:
                story_line = story.contents[0].replace("\n"," ").strip()
                #print(story.contents[0].replace("\n"," ").strip())
            open_file.write(story_line+"\n")
    
if __name__ == "__main__":
    main()
