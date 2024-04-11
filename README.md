This Python-based application is a configurable automated converter that transforms web-based books into an eBook/EPUB format. It mainly uses the libraries Requests, BeautifulSoup and EbookLib for the converting progess into EPUB.

# Requirements
> &GreaterGreater; 3.11.8 Python or higher

## Installing via requirements.txt
```bash
#!/bin/bash
git clone https://github.com/TheUnixDemon/Website2Book
cd ./Website2Book
pip install -r requirements.txt
```

# How to use
Before you can actually use the application for fetching a web book you have to create an configuration entry for your targeted server within the file `configurations/config.json`.  
Here to the [Server configuration Guide](CONFIG.md) and here to an [example](EXAMPLE.md) how it can looks like.

After the installation of all requirements and creating a configuration entry for you target server you can start the application via executing the file main.py.

```bash
#!/bin/bash
python main.py
```
