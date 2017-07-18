# YT_Description_Bot
# Bot that finds YouTube links in subs and comments with the Description

import praw
import requests

DIV = "\n" + ("~*" * 20)  # This is just a divider for printing

reddit = praw.Reddit('description_bot',
    user_agent='For grabbing and commenting with the YouTube Description')

print("logged in")

r = requests.get(input('type it > '))

def find_raw_description(rawtext):
    dopen = rawtext.find('>', rawtext.find('eow-description'))
    dclose = rawtext.find('</p>', dopen)
    return(rawtext[dopen+1:dclose])

def fix_links(rawtext):
    for chars in range(len(rawtext)):
        urlstart = rawtext.find('<a href="', chars)
        urlend = rawtext.find('"', urlstart)
        url = rawtext[urlstart+1:urlend]
        linktextS = rawtext.find('>', urlend)
        linktextE = rawtext.find('<', linktextS)
        linktext = rawtext[linktextS+1:linktextE]
        redlink = '[' + linktext + ']' + '(' + url + ')'
        textblock = rawtext[urlstart-9:linktextE+3]
        rawtext = rawtext.replace(textblock,redlink)
        chars = linktextE+3

def prettify_text(rawtext):
    #fix_links(rawtext)
    breaks = rawtext.split('<br />')
    for line in breaks:
        print(line)

rawtext = find_raw_description(r.text)
#prettify_text(rawtext)

print(rawtext)