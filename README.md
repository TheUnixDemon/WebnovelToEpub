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
python main.py --help
...
python main.py --title "Hollow Fantasy" --author "TheCreatorHimself" --cover "https://novelsite/hollowfantasy/hollowfantasycover.png" --url "https://novelsite/hollowfantasy/overview.html"
...
```

It's recommented for configuration purposes to use `--debug` for more informations about the current configuration status and it's responses to that. If you want to have a deeper view into the web scraper part you should use `--debughtml`. `--debughtml` shows the very process of the web scraper part related to your configuration. 

There are some other arguments like `--moreHumanLike`, `--humanLike`, `--latency` and `--timeout`. They all are related to the run-time.

`--timeout` is the only one of these that sets the timelimit of a connection. After the timelimit is reached the request runs into a timeout error and closes the connection and after some time reconnects with the server to try the connection again.

# Cookies
Everybody likes cookies! But websites love them a bit to much in my opinion. So I implemented a solution(even if not that clean and smooth). If a website gives the http error `403` as return, my program requests the user to put in a cookie in a text format. To get these cookies you should use your browser and get in the `inspect mode`.