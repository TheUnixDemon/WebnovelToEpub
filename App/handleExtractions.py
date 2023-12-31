import sys
from typing import List, Tuple

sys.path.append('extractions')

import contentExtractor
import requests
import titleExtractor


def makeExtractions(page: requests.Response) -> Tuple[str, List[str]]:
    # extract title
    titleEntry = titleExtractor.extractTitleEntry(page)  # get correct title entry(uncleared)
    chapterTitle = titleExtractor.finishTitleEntry(titleEntry)  # get cleared title

    # extract content
    chapterContent = contentExtractor.extractChapterContent(page)  # get cleared content

    return chapterTitle, chapterContent  # returns complete cleared chapter
