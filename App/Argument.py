import argparse

# for parameter arguments and general program controlling
class Argument:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog = "Website2Book - website scraper fetching & converting webnovels into ebooks",
            description = """
                Website2Book is a Python based application that targets simple webnovel sites.  
                It's fully configurable and targets simple webnovel sites with the purpose to create configs  
                for the wished websites even if those sites are new or unknown.
            """,
            epilog = "Configuration guide: https://github.com/TheUnixDemon/Website2Book/blob/main/CONFIG.md")
        
        parser.add_argument("-u", "--url", help = "url of chosen webnovel page", required = True)
        parser.add_argument("-t", "--title", help = "book title", required = True)
        parser.add_argument("-a", "--author", help = "name of author *optinal*", default = "Unknown")
        parser.add_argument("-c", "--cover", help = "cover for the ebook *optional*")
        parser.add_argument("-f", "--filename", help = "custom filename *optional*")
        parser.add_argument("-d", "--debug", action="store_true", help = "enable debug output", default = False)
        parser.add_argument("-D", "--debughtml", action="store_true", help = "enable debug output with html", default = False)
        self.__args: argparse = parser.parse_args()

        # ensure debug is enabled if debughtml is true
        if self.__args.debughtml:
            self.__args.debug = True

    def getUrl(self) -> str:
        return self.__args.url
    def getTitle(self) -> str:
        return self.__args.title
    def getAuthor(self) -> str:
        return self.__args.author
    def getCover(self) -> str:
        return self.__args.cover
    def getFilename(self):
        return (self.__args.filename if self.__args.filename else self.__args.title) + ".epub"
    def getDebug(self) -> bool:
        return self.__args.debug
    def getDebugHtml(self) -> bool:
        return self.__args.debughtml
    
    def returnArguments(self):
        print(f"url:{self.getUrl()}, title:{self.getTitle()}, author:{self.getAuthor()}, cover:{self.getCover()}, filename:{self.getFilename()}, debugmode:{self.getDebug()}")