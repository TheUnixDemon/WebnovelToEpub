import sys
import time

import bookmeta
import booksave
import handleExtractions
sys.path.append('requests')
import handleRequest
import requests
import userInteractions


def makeBook(bookTitle: str) -> None:
    session = requests.session()  # sets session for entire connection
    chapterURLs = bookmeta.returnChapterURLs()  # get all URLs within indexURL
    for i in range(0, len(chapterURLs)):  # one loop = one chapter
        URL = chapterURLs[i]

        while True:  # check if response is set or timeout
            page = handleRequest.makeRequest(URL, session)  # executes requests, handles 
            if page != False:  # no errors
                break

            elif page == False:  # reaction against timeout
                userInteractions.printTimeout()
                time.sleep(45)

        if page == None:  # URL is probably not correct | error 404
            userInteractions.printSkip()
            continue  # skip the URL

        chapterTitle, chapterContent = handleExtractions.makeExtractions(page)  # response = html page
        booksave.writeBook(bookTitle, chapterTitle, chapterContent)  # writes within a text file for progress saving

        userInteractions.printProgress(chapterURLs, i)  # i -> progress of chapters

    session.close()  # delete the session after extraction
