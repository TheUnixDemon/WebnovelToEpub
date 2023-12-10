from bs4 import BeautifulSoup
import html
import re

def extractChapterContent(page): # returns content as a list
    soup = BeautifulSoup(page.content, "html.parser")
    contentChapter = soup.find_all("p")

    flippedContent = [] # saved content in reversed order
    
    # must be splitted in reverse, because of the nesting of the <p> tags
    for i in range(len(contentChapter) -1, -1, -1): # one run is one reversed <p> tag
        splittedPhrases = str(contentChapter[i]).split("<p>")
        clearedPhrase = str(splittedPhrases[1]).replace("</p>", "") # only a string | clear the last tags within the phrase | [0] entries are only the <p> tags
        
        # filter if the phrase is a </script> tag
        if not re.search("</script>", clearedPhrase): # only add to list if not script tag
            fixedClearedPhrase = html.unescape(clearedPhrase) # replaces the wrong symbols
            flippedContent.append(fixedClearedPhrase)
        
    content = list(reversed(flippedContent)) # corrects the wrong order

    return content