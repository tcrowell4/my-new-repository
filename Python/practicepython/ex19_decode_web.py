import requests
from bs4 import BeautifulSoup
            
def main():
    print("main")
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    # loop through story headings and breakdown content

    for story in soup.find_all("p"):
        #print(story)
        print (story.get_text())
        #print(story.text.strip())


            
"""
    with open('ex21_write_a_file.txt', 'w') as open_file:
        for story in soup.find_all(class_="story-heading"):
            if story.a:
                story_line = story.a.text.replace("\n"," ").strip()
                #print(story.a.text.replace("\n"," ").strip())
            else:
                story_line = story.contents[0].replace("\n"," ").strip()
                #print(story.contents[0].replace("\n"," ").strip())
            open_file.write(story_line+"\n")
"""    
if __name__ == "__main__":
    main()
