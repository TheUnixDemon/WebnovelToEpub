import requests
import time
import json

class HttpHandler:
    def __init__(self, httpHeader: json):
        self.__session: requests = requests.session()
        self.__httpHeader = httpHeader
        
    def makeRequest(self, url: str) -> requests:
        try:
            time.sleep(1) # for timeout prevention
            page = self.__session.get(url, headers=self.__httpHeader)
            page.raise_for_status()
            return page
    
        except requests.exceptions.RequestException as e:
            return e.response.status_code # returns error code

    def handleErrors(self, response: requests, url: str = "") -> None:
        if isinstance(response, int): # int if not successfully
            match response:
                case 429:
                    print(f"<< RequestError -429- Timeout - wait 45 secounds [{url}] >>")
                    time.sleep(45)
                case 403:
                    print(f"<< RequestError -403- access forbidden [{url}] >>")
                    exit()
                case 404:
                    print(f"<< RequestError -404- not found [{url}] >>")
                case _:
                    print(f"<< RequestError -{response}- error code [{url}] >>")