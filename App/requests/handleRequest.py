import time
from typing import Union

import getHeaders
import requests
#import userInteractions


def makeRequest(URL: str, session: requests.Session) -> Union[requests.Response, bool, None]:  # will executed each url entry
    time.sleep(1)  # for lesser suspect behavoir
    try:
        header = getHeaders.getHeader()  # set basic header
        page = session.get(URL, headers=header)
        page.raise_for_status()

        return page  # returns html page if 200

    except requests.exceptions.RequestException as e:
        #userInteractions.printRequestError(URL, e)

        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 429:  # timeout error code
            return False
        else:
            return None
