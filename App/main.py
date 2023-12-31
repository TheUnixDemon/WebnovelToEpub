import bookmeta
import bookcreator
import booksave
import userInteractions

userInteractions.printStart()

def checkBooks():
    while True:
        bookTitle = input("Please enter the book filename: ")
        check = booksave.checkBook(bookTitle)
        
        if check == True:
            return bookTitle

bookTitle = checkBooks() # setted the bookTitle

bookmeta.createChapterURLs() # generating chapterURLs without check because of the timeout
bookcreator.makeBook(bookTitle) # get content of chapters within indexURL

userInteractions.printEnd()

