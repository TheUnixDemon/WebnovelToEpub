from bs4 import BeautifulSoup
import html
import re

def extractTitleEntry(page): # get correct title entry(uncleared)
    soup = BeautifulSoup(page.content, "html.parser")
    row_title = soup.find_all("meta")

    for i in range(len(row_title) -1, -1, -1): # flipped for loop
        if re.search('name="description"', str(row_title[i])): # for higher probability
            titleEntry = str(row_title[i]) # extracted title entry        
            break

    if titleEntry is None:
        titleEntry = "Chapter unknown"
    
    return titleEntry

def finishTitleEntry(titleEntry):
    # delete back end of the entry
    modifiedTitle = titleEntry.replace('" name="description"/>', '')

    # delete for end of of the entry
    pattern = re.compile(r'<meta content=".* - Chapter .*  - ')
    modifiedTitle = pattern.sub('', modifiedTitle) # almost finished title extraction
    
    # replace spezial symbols
    finishedTitle = html.unescape(html.unescape(modifiedTitle))
    
    return finishedTitle

