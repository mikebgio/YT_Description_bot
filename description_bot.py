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


def find_raw_description(rawtext):
    dopen = rawtext.find('>', rawtext.find('eow-description'))
    dclose = rawtext.find('</p>', dopen)
    return(rawtext[dopen + 1:dclose])


def find_links(rawtext):
    page = BeautifulSoup(rawtext, "html.parser")
    desc = page.find(id="eow-description")
    print(desc)

# def find_links(rawtext):
#     for link in BeautifulSoup(rawtext,
#                               "html.parser",
#                               parse_only=SoupStrainer('a')):
#         if link.has_attr('href'):
#             url = link['href']
#             linktext = link.string
#             redlink = '[' + linktext + ']' + '(' + url + ')'
#             link.unwrap()

def prettify_text(rawtext):
    breaks = find_links(rawtext)
    breaks = rawtext.split('<br />')
    for line in breaks:
        print(line)


rawtext = find_raw_description(r.text)
prettify_text(rawtext)

# print(rawtext)
