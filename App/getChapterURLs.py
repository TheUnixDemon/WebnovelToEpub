import getChapterlist
import sys
sys.path.append('configs')
import getConfig
import json

def getChapterURLs():
    URL = input("Please enter URL of the book: ")
    chapterlist = getChapterlist.getChapterlist(URL) # chapterlist is a website and its content are the chapter urls
    print(chapterlist)
    
getChapterlist()