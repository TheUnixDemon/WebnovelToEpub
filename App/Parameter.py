import argparse

# for parameter arguments and general program controlling
class Parameter:
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
        parser.add_argument("-a", "--author", help = "name of author *optinal*")
        parser.add_argument("-c", "--cover", help = "cover for the ebook *optional*")
        parser.add_argument("-f", "--filename", help = "custom filename *optional*")
        self.args: argparse = parser.parse_args()
    
    def getUrl(self):
        return self.args.url
    def getTitle(self):
        return self.args.title
    def getAuthor(self):
        return self.args.author if self.args.author else "Unknown"
    def getCover(self):
        return self.args.cover
    def getFilename(self):
        return (self.args.filename if self.args.filename else self.args.title) + ".epub"
    
    def returnArguments(self):
        print(f"URL:{self.getUrl()}, Title:{self.getTitle()}, Author:{self.getAuthor()}, Cover:{self.getCover()}, Filename:{self.getFilename()}")