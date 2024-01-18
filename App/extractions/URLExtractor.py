import sys

import json
import re

import requests
from bs4 import BeautifulSoup

sys.path.append("requests")
import handleRequest

def usePatterns(ServerConfig: json, soup: BeautifulSoup) -> list:
    patternConfig = ServerConfig["request"]["pattern"]["chapterlist"]
    patternKeys = ["class", "url", "prefix", "suffix"]
    
    elements = ""
    urlPattern = ""
    prefix = ""; suffix = "" # default is empty
    for patternKey in patternKeys:
        if patternKey in patternConfig: # checks if the key is within the dic
            value = patternConfig[patternKey]
            match patternKey:
                case "class": # filters all after the declared HTML class
                    elements = soup.find_all(class_=value)
                case "url": # sets patterns for href link
                    urlPattern = value
                case "prefix": 
                    prefix = value
                case "suffix":
                    suffix = value    
    
    chapterURLs = []
    if elements: # class pattern is set
        for element in elements:
            a_tags = element.find_all("a")
            for a_tag in a_tags:
                href = a_tag.get("href")
                chapterURLs.append(prefix + str(href) + suffix)
    else:
        a_tags = soup.find_all("a")
        for a_tag in a_tags:
            href = a_tag.get("href")
            chapterURLs.append(prefix + str(href) + suffix)
    
    filteredChapterURLs = [] # with the 
    if urlPattern: # url pattern is set
        for chapterURL in chapterURLs:
            if re.search(urlPattern, chapterURL): # adds to filtered list if pattern is true
                filteredChapterURLs.append(chapterURL)
        chapterURLs = filteredChapterURLs # overrides old chapterURLs with filtered version
    
    return chapterURLs

# extracts the chapterURLs from the chapterlist pages
def extractChapterURLs(serverConfig: json, URL: str) -> list:
    print(serverConfig, URL)
    session = requests.session()
     
    page = handleRequest.makeRequest(URL, session)
    soup = BeautifulSoup(page.content, "html.parser")
    
    if "pattern" in serverConfig["request"]:  # only if some optional patterns are set
        if "chapterlist" in serverConfig["request"]["pattern"]:
            chapterURLs = usePatterns(serverConfig, soup) 
    else:
        chapterURLs = []
        a_tags = soup.find_all("a")
        for a_tag in a_tags:
            href = a_tag.get("href")
            chapterURLs.append(str(href)) # must be translated into a str 'cause is b4s type

    session.close()

    return chapterURLs
