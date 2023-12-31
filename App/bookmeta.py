from pathlib import Path
import re


def createChapterURLs():
    uncleared_url = input("html adress of a chapter: ")
    url = re.sub(r"_.*\.html", "_", uncleared_url)  # finds out the right base url

    print("")
    minNum = input("Start chapter number: ")
    maxNum = input("Final chapter number: ")
    print("")

    chapterURL = []  # saves all created chatperURLs
    for i in range(int(minNum), int(maxNum) + 1):  # +1 for a correct final number
        chapterURL.append(url + str(i) + ".html")

    # writes the chaterURLs within "chaterindex"
    myfile = Path("./indexURL.txt")
    myfile.touch(exist_ok = True)
    f = open(myfile)

    my_save = open("indexURL.txt", "w")
    for line in chapterURL:
        my_save.write(line + "\n")

    my_save.close()


def returnChapterURLs():  # returns all URLs as list
    chapterURLs = []
    my_save = open("indexURL.txt", "r")
    lines = my_save.read().splitlines()

    for line in lines:
        chapterURLs.append(line)

    my_save.close()

    return chapterURLs
