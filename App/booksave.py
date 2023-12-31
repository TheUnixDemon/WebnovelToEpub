import userInteractions

import os
from pathlib import Path

def checkBook(bookTitle):  # check if a book with the same name exists
    filename = str(bookTitle) + ".html"
    fullPath = os.path.join("../Books/HTML", filename)

    if os.path.exists(fullPath):
        userResponse = userInteractions.printNameError()
        if userResponse == True:
            os.remove(fullPath)
            return True

        else:
            return False
    else:
        return True

def writeBook(bookTitle, chapterTitle, chapterContent):  # saves it as a .txt/markdown | append one chapter
    # sets the variables once more for a better understanding of the meanings
    filename = str(bookTitle) + ".html"
    phrases = chapterContent

    fullPath = os.path.join("../Books/HTML", filename)
    with open(fullPath, "a") as book:
        book.write('\n\n<h1 class="chapter">' + chapterTitle + '</h1>\n')

        for line in phrases:
            book.write("\n<p>" + line + "</p>")