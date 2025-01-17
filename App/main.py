import requests
import json
import os

from ConfigVerify import ConfigVerify
from ConfigHandler import ConfigHandler

from HttpHandler import HttpHandler
from FetchChapterURLs import FetchChapterURLs
from FetchChapterContent import FetchChapterContent
from CreateEPUB import CreateEPUB

import userInput

# checks needed folder
folderConfig: str = "configurations/"
if not os.path.exists(folderConfig):
    print("<< Locale folder named 'configurations/' is needed >>")
    exit()

# verify json configurations via schema
verify = ConfigVerify()
verify.Config()
verify.defaultHttpHeader()

# user input < URL to book
while True:
    url: str = input("Please enter the URL of the book's main page: ")
    if userInput.validateCommonInput(url): # returned true | no errors
        break
    
# load/set configurations
config = ConfigHandler(url)
serverConfig: json = config.getServerConfig()
requestConfig: json = serverConfig["request"] # new mapping
serverHttpHeader: json = config.getServerHttpHeader()

# gets server type (extern = true or intern = false)
typeServer: bool = requestConfig["params"].get("type", True)

# creates request instance
httpRequest = HttpHandler(serverHttpHeader)

# get chapterURLs
fetchURLs = FetchChapterURLs(httpRequest, requestConfig, typeServer, url)
chapterURLs: list[str] = fetchURLs.getChapterURLs()

# select chapters
selectedChapterURLs: list[str] = userInput.selectChapters(chapterURLs)

print("--- Please enter book related metadata ---")
while True:
    bookTitle: str = input("Title: ")
    if userInput.validateCommonInput(bookTitle):
        break
bookFilename: str = userInput.getFilename()
bookAuthor: str = input("Author: ")

if bookAuthor:
    makeEPUB = CreateEPUB(bookTitle, bookFilename, bookAuthor)
else:
    makeEPUB = CreateEPUB(bookTitle, bookFilename)

bookCoverImageURL: str = input("Cover Image URL: ")

if bookCoverImageURL:
    coverImage: requests.Response = httpRequest.makeRequest(bookCoverImageURL)
    makeEPUB.addCover(coverImage)

print("--- Fetching book ---")
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