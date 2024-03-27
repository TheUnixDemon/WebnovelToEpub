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

    def handleErrors(self, response: requests) -> None:
        if isinstance(response, int): # is int if not successfully
            match response:
                case 429:
                    print("<< -429- Timeout - wait 45 secounds >>")
                    time.sleep(45)
                case 403:
                    print("<< -403- Bot has been detected - access is forbidden >>")
                    exit()