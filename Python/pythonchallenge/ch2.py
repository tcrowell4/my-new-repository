import requests
from bs4 import BeautifulSoup, Comment

def find_rare(str):
    x = ""
    for char in str:
        if char.isalpha():
            x = x + char
    print("x = %s" % x)
            
def main():
    print("main")
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    # loop through story headings and breakdown content

    #print(soup.prettify())
    
    """<!--
    find rare characters in the mess below:
    -->
    <!--
    %%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
    %&]!{{%*_!*}&)}$**_{*!#%[[#]!](^^$![#[[*}%(_#^^!%))!_^@)@**@}}(%%{#*%@(((]^%^![&
    }!)$]&($)@](+(#{$)_%^%_^^#][{*[)%}+[##(##^{$}^]#&(&*{)%)&][&{]&#]}[[^^&[!#}${@_(
    #@}&$[[%]_&$+)$!%{(}$^$}*
    -->

    """

    for comments in soup.find_all(text=lambda text:isinstance(text, Comment)):
        print("Comments")
        #print(comments)
        find_rare(comments.extract())
        #print (x)
        #print(story.text.strip())
        
    """
    Comments
    x = findrarecharactersinthemessbelow
    Comments
    x = equality
    """
        

            
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
