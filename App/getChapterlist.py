import requests
import json
import sys
import re

sys.path.append('configs')
import getConfig
import userInteractions

def getServerConfig(config: json, URL: str): # gets spezific server configuration
    # for identification of the server URL
    for i in range(0, len(config)):
        if re.search(str(config[i]["server"]), URL):
            return config[i]

def getId(requestConfig: json, URL: str) -> list:
    idKey: str = requestConfig["params"]["id"] # sets key and rules the filter
    filter: str = requestConfig["filter"]
    
    # for editing of the known book URL
    filterEntries = filter.split("{}")
    
    # editing the URL of the choosen book
    delBegin = URL.replace(filterEntries[0], "")
    delEnd = delBegin.split(filterEntries[1])
    idValue = delEnd[0] # extracted id value
    
    return [idKey, idValue]
        
def genURL(serverConfig: json, URL: str) -> list:
    requestConfig: json = serverConfig["request"]
    contentURL = requestConfig["url"] + "?"
    page = False
    
    # adds parameters to the contentURL
    for key, value in requestConfig["params"].items():
        match key:
            case "id":
                id = getId(requestConfig, URL)
                contentURL += id[0] + "=" + id[1] + "&"
            case "page": # will be outsourced within a other function
                page = True
            case _: # special case for additional parameters
                contentURL += str(key) + "=" + str(value) + "&"
         
    # deletes useless "&" variables form the URL
    if contentURL.endswith("&"):
        contentURL = contentURL[:-1]
          
    # checks the URLs if they are reacheably
    session = requests.session()  
    if page is True: # adds the page parameter
        contentURLs = []
        for i in range(0, 10):
            pageRelatedURL = contentURL + requestConfig["params"]["page"] + "=" + str(i) # for chapterLists with more than one site
            contentURLs.append(pageRelatedURL)
        return contentURLs
    else:
        return contentURL
        
        
def getChapterlist(URL: str):
    serverConfig: json = getConfig.getServerConfig(URL) 
    contentURL = genURL(serverConfig, URL) # creates the ChapterlistURLs
    return contentURL

print(getChapterlist("https://novelbin.me/novel-book/the-kings-avatar#tab-chapters-title"))