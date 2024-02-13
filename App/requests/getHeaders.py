from typing import Dict


def getHeader():  # for a more browser like appearance(can hide bot attibutes)
    default = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        # Hier kann auch 'gzip, deflate' verwendet werden, falls Brotli nicht unterstützt wird
        'Accept-Encoding': 'br',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Accept-Charset': 'utf-8',  # Hier wird die Zeichenkodierung spezifiziert
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0'
    }

    return default
