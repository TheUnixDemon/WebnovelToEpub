import json

# creates a basic url to the chapterlist that containtes the chapterurls(without paging)
class FetchChapterList:
    def __init__(self, requestConfig: json, typeServer: bool, url: str):
        self.__requestConfig = requestConfig
        self.__typeServer = typeServer
        self.__url = url
        
        # generating base url for external or internal requests
        self.setChapterListURL()
    
    def getBookId(self) -> str:
        # sets variables for fetching the id value
        filter: str = self.__requestConfig.get("filter")
        url: str = self.__url
        # parts that will be deleted from the input url
        filterPatterns: list[str] = filter.split("{}")
        # deletes all around but the id value
        removeBegin: str = url.replace(filterPatterns[0], "") # deletes before the brachets
        splitEnd: list[str] = removeBegin.split(filterPatterns[1])
        bookId: str = splitEnd[0]
        return bookId
    
    def setChapterListURL(self) -> str: # is the base for the url to chapterlist
        urlBase: str = self.__requestConfig.get("url", None)
        if self.__typeServer is True:
            urlBase += "?"
        
            # adds id param for chosen book ?id=id
            if "id" in self.__requestConfig["params"]:
                idParam: str = self.__requestConfig["params"].get("id") + "=" + self.getBookId()
                urlBase += idParam + "&"
                
            # for common additional keys
            keys = ["add"]
            for key in keys: # adds basic parameters
                if key in self.__requestConfig["params"]:
                    urlBase += self.__requestConfig["params"].get(key) + "&"
                
        elif self.__typeServer is False:
            urlBase = urlBase.replace("{}", self.getBookId()) # puts bookId into needed url /id/

        # deletes useless & symbol
        if urlBase.endswith("&") or urlBase.endswith("?"):
            urlBase = urlBase[:-1]
        # sets url
        self.__chapterListURL: str = urlBase
        
    def getChapterListURL(self) -> str:
        return self.__chapterListURL