# YT_Description_Bot
# Bot that finds YouTube links in subs and comments with the Description

import praw
import requests
from bs4 import BeautifulSoup, SoupStrainer

DIV = "\n" + ("~*" * 20)  # This is just a divider for printing

reddit = praw.Reddit('description_bot',
                     user_agent='For grabbing and commenting with the YouTube Description')

print("logged in")

r = requests.get(input('type it > '))

def get_description(rawtext):
    page = BeautifulSoup(rawtext, "html.parser")
    description = page.find(id="eow-description")
    for br in description.find_all("br"):
        br.replace_with("\n")
    return(description.get_text())



# rawtext = find_raw_description(r.text)
# prettify_text(rawtext)
get_description(r.text)

# print(rawtext)
