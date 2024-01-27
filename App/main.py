import bookcreator
import bookmeta
import booksave
import userInteractions

import re
from pathlib import Path

import chapterURLs as genChapterURLs
import userInteractions



userInteractions.printStart()


def checkBooks() -> str:
    while True:
        bookTitle = input("Please enter the book filename: ")
        check = booksave.checkBook(bookTitle)

        if check:
            return bookTitle
        else:
            print("HTML data with the same name detected")


bookTitle = checkBooks()  # setted the bookTitle

bookmeta.createChapterURLs()  # generating chapterURLs without check because of the timeout
bookcreator.makeBook(bookTitle)  # get content of chapters within indexURL

#userInteractions.printEnd()
