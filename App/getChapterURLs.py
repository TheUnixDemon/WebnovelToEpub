import getChapterlist
import sys
sys.path.append('configs')
import getConfig
import json

import requests
from bs4 import BeautifulSoup

def get_links_in_li(url):
    try:
        # HTTP-Anfrage an die Webseite senden
        response = requests.get(url)
        
        # Sicherstellen, dass die Anfrage erfolgreich war (Status-Code 200)
        response.raise_for_status()
        
        # HTML-Inhalt der Webseite mit BeautifulSoup parsen
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Alle HREFs innerhalb von <li>-Tags extrahieren
        links = [li.a['href'] for li in soup.find_all('li') if li.a and li.a.get('href')]
        
        return links

    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")
        return []

# Beispielaufruf
url = 'https://www.wuxiamate.com/e/extend/fy.php?wjm=the-primal-hunter&X-Requested-With=XMLHttpRequest&page=0'
links_in_li = get_links_in_li(url)

# Ausgabe der extrahierten Links vor der Schleife
print("Extrahierte Links:")
print(links_in_li)

# Schleife zur Ausgabe der Links
for link in links_in_li:
    print(link)

def getChapterURLs():
    URL = input("Please enter URL of the book: ")
    chapterlist = getChapterlist.getChapterlist(URL) # chapterlist is a website and its content are the chapter urls
    print(chapterlist)