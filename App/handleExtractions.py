import sys
from typing import List, Tuple

sys.path.append("extractions")
sys.path.append("configs")

import contentExtractor
import requests
import titleExtractor
import json
import handleConfig

def makeExtractions(serverConfig: json, page: requests.Response):
    # extract title
    chapterTitle = titleExtractor.extractTitle(serverConfig, page)

    # extract content
    chapterContent = contentExtractor.extractChapterContent(page)  # get cleared content

    return chapterTitle, chapterContent  # returns complete cleared chapter
