import requests
import random
import time

# makes the requests, handles the header(encode into utf-8) and 
class HttpHandler:
    def __init__(self, httpHeader: dict[str], timeout: int, timeoutEach: list[int], selfReferer: bool):
        self.__session: requests = requests.session()
        self.__httpHeader: dict[str] = {}
        self.setHttpHeader(httpHeader)
        self.__timeout = timeout
        # implemented for encoding 'cause 
        self.__timeoutEach: list[int] = None
        if timeoutEach: # not None 
            self.__timeoutEach: list[int] = [timeoutEach[0], timeoutEach[1]]
        self.__selfReferer: bool = selfReferer

    def setHttpHeader(self, httpHeader: dict[str]) -> None:
        self.__httpHeader = {}
        for key, value in httpHeader.items():
            self.__httpHeader[key] = value.encode("utf-8")

    # makes the request with the given header, timeout beaviour, session and so on
    def makeRequest(self, url: str) -> requests:
        # timeout for each request for more humanlike behavore; lesser probability to run to a http timeout
        if self.__timeoutEach:
            duration: int
            if self.__timeoutEach[0] != self.__timeoutEach[1]:
                duration = self.getDuration(self.__timeoutEach[0], self.__timeoutEach[1])
            else: # static duration a = b
                duration = self.__timeoutEach[0]
            time.sleep(duration)
        # if selfReferer in config.json is true
        if self.__selfReferer:
            self.__httpHeader["Referer"] = url.encode("utf-8")
        try:
            page = self.__session.get(url, headers = self.__httpHeader, timeout = self.__timeout)
            page.raise_for_status()
            return page
        # time limit for request reached; timeout or server error suspected
        except requests.exceptions.Timeout:
            timeout: int = 30
            # not None and not static; a != b
            if self.__timeoutEach and self.__timeout[0] != self.__timeout[1]: 
                timeout += self.getDuration(0, 5) # for more humanlike beahviour
            print(f"<< RequestError time limit *{self.__timeout}* reached - wait {timeout} secounds [{url}] >>")
            time.sleep(timeout)
        # http errors - non timeout errors(probably)
        except requests.exceptions.RequestException as e:
            status: int = e.response.status_code # http error code
            match status:
                # critical error; exits the program
                case 403:
                    print(f"<< RequestError -403- access forbidden [{url}] >>")
                    # adds a new cookie if error 403; if its successful fetching can be processeded
                    while True:
                        cookie: str = input("New Cookie needed?(only value):").strip()
                        if cookie:
                            self.__httpHeader["Cookie"] = cookie.encode("utf-8")
                            break
                # non critical error; can be handled by
                case 404:
                    print(f"<< RequestError -404- not found [{url}]")
                case _:
                    print(f"<< RequestError -{status}- error code [{url}]")    
            return status
        
    # method is mostly detiminated by arguments like humanlike, morehumanlike and latency
    def getDuration(self, a: int, b: int) -> int:
        return random.randint(a, b) # if a=0, b=5 -> 0-5 (both included)
    
    # after all data are collected
    def closeSession(self):
        self.__session.close()