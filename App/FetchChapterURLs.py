from bs4 import BeautifulSoup
import requests
import json
import re

from FetchChapterList import FetchChapterList
from HTMLSearch import HTMLSearch

# uses FetchChapterLists base chapterlist, modifies it and fetches the chapterurls
class FetchChapterURLs(FetchChapterList):
    def __init__(self, httpRequest: requests, requestConfig: json, typeServer: bool, url: str):
        super().__init__(requestConfig, typeServer, url)
        self.__chapterListURL = super().getChapterListURL()
        self.__requestConfig = requestConfig
        self.__httpRequest = httpRequest
        self.__chapterURLs: list[str] = []
        self.__HTMLpraser = HTMLSearch() 
        self.setChapterURLs()

    # will be executed by self.setChapterURLs to get the urls within chapterlist
    def fetchChapterURLs(self, response: requests) -> list[str]: # fetches the urls out of the chapterlist page/s
        patternChapterList = self.__requestConfig["pattern"]["chapterlist"]
        soup = BeautifulSoup(response.content, "html.parser")
        self.__HTMLpraser.setSoup(soup)
        
        # get section
        classHtml: str = patternChapterList.get("class", None)
        idHtml: str = patternChapterList.get("id", None)
        if classHtml or idHtml:
            self.__HTMLpraser.searchSection(classHtml, idHtml)
            
        # find elements (within section)
        tagHtml: str = patternChapterList.get("tag", "a")
        tagClassHtml: str = patternChapterList.get("tagClass", None)
        tagIdHtml: str = patternChapterList.get("tagId", None)
        if tagHtml or tagClassHtml or tagIdHtml:
            self.__HTMLpraser.searchElements(tagHtml, tagClassHtml, tagIdHtml)
        
        # other patterns
        attribute: str = patternChapterList.get("attribute", "href")
        prefix: str = patternChapterList.get("prefix", "")
        suffix: str = patternChapterList.get("suffix", "")
        urlPattern: str = patternChapterList.get("urlPattern", None)
        
        # find_all -> list format
        chapterURLs: list[str] = []
        elements = self.__HTMLpraser.getSoup()
        for element in elements: # one element = one link
            if urlPattern:
                if not re.search(urlPattern, element):
                   continue
            attributeValue = element.get(attribute)
            chapterURL: str = prefix + attributeValue + suffix
            chapterURLs.append(chapterURL)
        return chapterURLs

    def setChapterURLs(self) -> None:
        # creates instance for b4s
        paramPage: str = self.__requestConfig["params"].get("page", None)  # sets if only one chapterlist or more
        chapterListURL: str = self.__chapterListURL
        if paramPage: # if page is set
            paramPageStart: int = self.__requestConfig["params"].get("pageStart", 0) # sets the first page number (PAGE=0)
            x: int = paramPageStart
            while (True):
                chapterListURLPage = chapterListURL + paramPage + str(x) # link to one of many chapterlists
                response = self.__httpRequest.makeRequest(chapterListURLPage)
                if isinstance(response, int): # checks if errors did happen
                    self.__httpRequest.handleErrors(response, chapterListURLPage)
                    if response == 404: # not reachable -> expection: last list passed
                        print("<< RequestError -404- is a common expection and can be ignored normally >>")
                        break
                else:
                    pageChapterURLs: list[str] = self.fetchChapterURLs(response)
                    if len(pageChapterURLs) == 0: # contains no links -> expection: only empty lists are remaining
                        break
                    self.__chapterURLs.extend(pageChapterURLs)
                x += 1 # goes to the next page
        else: # page is not set
            response = self.__httpRequest.makeRequest(chapterListURL)
            if isinstance(response, int):
                self.__httpRequest.handleErrors(response, chapterListURL)
            else:
                chapterURLs: list[str] = self.fetchChapterURLs(response)
                self.__chapterURLs = chapterURLs
        
    # returns fetched(by setChapterURLs) chapterUrls
    def getChapterURLs(self) -> list[str]:
        return self.__chapterURLs