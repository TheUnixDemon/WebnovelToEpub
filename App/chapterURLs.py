import requests
import json
import sys
import re

sys.path.append("configs")
import handleConfig
import userInteractions
sys.path.append("extractions")
import URLExtractor

def getId(requestConfig: json, URL: str) -> list: # mostly the name of the book
    idKey: str = requestConfig["params"]["id"] # sets key and rules the filter
    filter: str = requestConfig["filter"]
    
    # for editing of the known book URL
    filterEntries = filter.split("{}")
    
    # editing the URL of the choosen book
    delBegin = URL.replace(filterEntries[0], "")
    delEnd = delBegin.split(filterEntries[1])
    idValue = delEnd[0] # extracted id value
    return [idKey, idValue]


def getURLs(serverConfig: json, URL: str) -> list:
    requestConfig: json = serverConfig["request"]
    contentURL = requestConfig["url"] + "?"
    page = False
    
    # adds parameters to the contentURL
    for key, value in requestConfig["params"].items():
        match key:
            case "id":
                id = getId(requestConfig, URL)
                contentURL += id[0] + "=" + id[1] + "&"
            case "page": # will be outsourced within another function
                page = True
            case "add": # special case for additional parameters
                contentURL += value[0] + "=" + value[1] + "&"
         
    # deletes useless "&" variables form the URL
    if contentURL.endswith("&"):
        contentURL = contentURL[:-1]
          
    chapterURLs = [] # will be extended or replaced
    if page is True: # adds the page variable | more than one chapterlist pages
        i = 0
        while(True):
            pageRelatedURL = contentURL + requestConfig["params"]["page"] + "=" + str(i) # for chapterLists with more than one site
            extractedChapterURLs: list = URLExtractor.extractChapterURLs(serverConfig, pageRelatedURL)
            if extractedChapterURLs: # checks if the chapterlist page is empty
                chapterURLs.extend(extractedChapterURLs)
                i += 1
            else: # cancels the while if page is empty
                return chapterURLs
    else: # expects only one chapterlist page with all chapter urls
        return URLExtractor.extractChapterURLs(serverConfig, contentURL)
        
def getChapterURLs(URL: str) -> list:
    serverConfig: json = handleConfig.getServerConfig(URL) # gets server spezific configuration
    chapterURLs = getURLs(serverConfig, URL) # creates the ChapterlistURL/s
    
    return chapterURLs