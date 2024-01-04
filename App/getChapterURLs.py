import handleConfig

def getChapterURLs() -> list:
    URL = input("Please enter URL of the book: ")
    chapterlist = handleConfig.getChapterlist(URL) # chapterlist is a website and its content are the chapter urls
    print(chapterlist)
    
getChapterURLs()