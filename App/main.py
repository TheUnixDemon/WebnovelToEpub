import requests
import json
import os

from Argument import Argument
from ConfigVerify import ConfigVerify
from ConfigHandler import ConfigHandler

from HttpHandler import HttpHandler
from FetchChapterURLs import FetchChapterURLs
from FetchChapterContent import FetchChapterContent
from CreateEPUB import CreateEPUB

import chapterSelection

# sets parameter arguments
param: Argument = Argument()

# checks needed folder
folderConfig: str = "configurations/"
if not os.path.exists(folderConfig):
    print("<< Locale folder named 'configurations/' is needed >>")
    exit()

# verify json configurations via schema
verify = ConfigVerify()
verify.Config()
verify.defaultHttpHeader()
    
# prints out current parameter arguments
param.returnArguments()

# load/set configurations
config = ConfigHandler(param.getUrl())
serverConfig: json = config.getServerConfig()
requestConfig: json = serverConfig["request"] # new mapping
serverHttpHeader: json = config.getServerHttpHeader()

# gets server type (extern = true or intern = false)
typeServer: bool = requestConfig["params"].get("type", True)
if param.getDebug():
    print(f"<< ServerType:{typeServer} -CONFIG- -DEBUGMODE- >>")

# creates request instance
httpRequest = HttpHandler(serverHttpHeader)

# get chapterURLs
if param.getDebug():
    print(f"<< starting fetching process of chapterlist and it's chapter urls -DEBUGMODE- >>")
fetchURLs = FetchChapterURLs(httpRequest, requestConfig, typeServer, param.getUrl(), param.getDebug(), param.getDebugHtml())
chapterURLs: list[str] = fetchURLs.getChapterURLs()
if param.getDebug():
    print("<< chapterlist fetching process is finished -DEBUGMODE- >>")

# select chapters via external function
selectedChapterURLs: list[str] = chapterSelection.selectChapters(chapterURLs)

if param.getDebug():
    print("<< creating ebook and adding metadata(title, filename, author, cover, ...) -DEBUGMODE- >>")
# sets metadata for ebook file
makeEPUB = CreateEPUB(param.getTitle(), param.getFilename(), param.getAuthor())
if param.getCover():
    coverImage: requests.Response = httpRequest.makeRequest(param.getCover())
    if isinstance(coverImage, int):
        httpRequest.handleErrors(coverImage, param.getCover())
        print(f"<< Cover image [{param.getCover}] can't be used >>")
    else:
        makeEPUB.addCover(coverImage)

print("--- Creating ebook ---")
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
        print("Saving progress: " + str(round(progressInPercent, 2)) + " %")
    else:
        print("<< Error: No content found at current page >>")
    chapterCounter += 1
makeEPUB.writeBook()
print("--- Done ---")