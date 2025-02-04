import argparse
import requests
import json
import os

from Parameter import Parameter
from ConfigVerify import ConfigVerify
from ConfigHandler import ConfigHandler

from HttpHandler import HttpHandler
from FetchChapterURLs import FetchChapterURLs
from FetchChapterContent import FetchChapterContent
from CreateEPUB import CreateEPUB

import chapterSelection

# parameter arguments
param: Parameter = Parameter()

print(f"URL:{param.getUrl()}")
print(f"Author")
print(f"Title")
print(f"Filename")

# checks needed folder
folderConfig: str = "configurations/"
if not os.path.exists(folderConfig):
    print("<< Locale folder named 'configurations/' is needed >>")
    exit()

# verify json configurations via schema
verify = ConfigVerify()
verify.Config()
verify.defaultHttpHeader()
    
# load/set configurations
config = ConfigHandler(param.getUrl())
serverConfig: json = config.getServerConfig()
requestConfig: json = serverConfig["request"] # new mapping
serverHttpHeader: json = config.getServerHttpHeader()

# gets server type (extern = true or intern = false)
typeServer: bool = requestConfig["params"].get("type", True)

# creates request instance
httpRequest = HttpHandler(serverHttpHeader)

# get chapterURLs
fetchURLs = FetchChapterURLs(httpRequest, requestConfig, typeServer, param.getUrl())
chapterURLs: list[str] = fetchURLs.getChapterURLs()

# select chapters
selectedChapterURLs: list[str] = chapterSelection.selectChapters(chapterURLs)

# sets metadata for ebook file
makeEPUB = CreateEPUB(param.getTitle(), param.getFilename(), param.getAuthor())
if param.getCover():
    coverImage: requests.Response = httpRequest.makeRequest(param.getCover())
    makeEPUB.addCover(coverImage)

print("--- creating ebook ---")
# get content & make book files
chapterCounter: int = 1 # show progess
fetchContent = FetchChapterContent(httpRequest, requestConfig)
for chapterURL in selectedChapterURLs:
    # gets content as plain text (no html format)
    fetchContent.setChapter(chapterURL) # sets response content as chapter
    # returns content converted as plain text/string
    chapterTitle: str = fetchContent.getChapterTitle()
    chapterContent: list[str] = fetchContent.getChapterContent()
    if len(chapterTitle) > 0 and len(chapterContent) > 0: # checks if content is found
        makeEPUB.addChapter(chapterTitle, chapterContent)
        progressInPercent: float = ((chapterCounter / len(selectedChapterURLs)) * 100)
        print("Saving progress: " + str(round(progressInPercent, 1)) + " %")
    else:
        print("<< Error: No content found at current page >>")
    chapterCounter += 1
makeEPUB.writeBook()
print("--- Done ---")