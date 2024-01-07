import re
from pathlib import Path

import chapterURLs as genChapterURLs
import userInteractions

def chapterDecision(chapterURLs: list) -> list:
    userInteractions.chapterDecision(chapterURLs)
    
    start = int(input("Please set a start chapter: ")) - 1
    end = int(input("Please set a end chapter: "))
    print("")
    return [start, end]

def createChapterURLs() -> None:
    URL: str = input("html adress of the book: ")
    chapterURLs = genChapterURLs.getChapterURLs(URL) # extracts all chapter URLs with the configs
    chapterRange = chapterDecision(chapterURLs) # sets the chapters that should be saved

    chosenChapters = []  # saves all created chatperURLs
    for i in range(chapterRange[0], chapterRange[1]):  # +1 for a correct final number
        chosenChapters.append(chapterURLs[i])

    # writes the chaterURLs within "chaterindex"
    myfile = Path("./indexURL.txt")
    myfile.touch(exist_ok = True)
    f = open(myfile)

    my_save = open("indexURL.txt", "w")
    for line in chosenChapters:
        my_save.write(line + "\n")

    my_save.close()


def returnChapterURLs() -> list:  # returns all URLs as list
    chapterURLs = []
    my_save = open("indexURL.txt", "r")
    lines = my_save.read().splitlines()

    for line in lines:
        chapterURLs.append(line)

    my_save.close()

    return chapterURLs