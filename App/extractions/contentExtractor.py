import html
import re
from typing import List

import requests
from bs4 import BeautifulSoup


# returns content as a list
def extractChapterContent(page: requests.Response) -> List[str]:
    soup = BeautifulSoup(page.content, "html.parser", from_encoding="utf-8")
    contentChapter = soup.find_all("p")

    flippedContent: List[str] = []  # saved content in reversed order

    # must be splitted in reverse, because of the nesting of the <p> tags
    for i in range(len(contentChapter) - 1, -1, -1):  # one run is one reversed <p> tag
        splittedPhrases = str(contentChapter[i]).split("<p>")
        # only a string | clear the last tags within the phrase | [0] entries are only the <p> tags
        clearedPhrase = str(splittedPhrases[1]).replace("</p>", "")

        # filter if the phrase is a </script> tag
        if not re.search("</script>", clearedPhrase):  # only add to list if not script tag
            fixedClearedPhrase = html.unescape(
                clearedPhrase)  # replaces the wrong symbols
            flippedContent.append(fixedClearedPhrase)

    content = list(reversed(flippedContent))  # corrects the wrong order

    return content
