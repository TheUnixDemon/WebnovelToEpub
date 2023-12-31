from typing import Dict


def getHeader() -> Dict[str, str]:  # for a more browser like appearance(can hide bot attibutes)
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'identity',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    return header
