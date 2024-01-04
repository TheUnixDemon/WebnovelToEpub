import requests
import json
import sys
import re

import getConfig
sys.path.append('requests')
import handleRequest
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
          
    # checks the URLs if they are reacheably
    session = requests.session()  
    if page is True: # adds the page parameter
        contentURLs = []
        i = 0
        while(True):
            pageRelatedURL = contentURL + requestConfig["params"]["page"] + str(i) # for chapterLists with more than one site
            request = handleRequest.makeRequest(pageRelatedURL, session)  # executes requests, handles 
            if request:  # no errors
                contentURLs.append(pageRelatedURL)
                print(pageRelatedURL)
            else: # expects all chapter pages are written within the contentURLs
                return contentURLs
            i = i + 1
    else:
        request = handleRequest.makeRequest(contentURL, session)
        if request:
            return contentURL
        
        
def getChapterlist(URL: str):
    config: json = getConfig.getConfig()
    serverConfig: json = getServerConfig(config, URL) 

    contentURL = genURL(serverConfig, URL)
    return contentURL