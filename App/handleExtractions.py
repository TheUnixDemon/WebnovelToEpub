import sys
sys.path.append('extractions')

import titleExtractor
import contentExtractor


def makeExtractions(page):
    # extract title
    titleEntry = titleExtractor.extractTitleEntry(page)  # get correct title entry(uncleared)
    chapterTitle = titleExtractor.finishTitleEntry(titleEntry)  # get cleared title

    # extract content
    chapterContent = contentExtractor.extractChapterContent(page)  # get cleared content

    return chapterTitle, chapterContent  # returns complete cleared chapter
