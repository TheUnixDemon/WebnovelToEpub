Every configuration file lays within the folder `configurations/`.

`config.json` is for server based configuration. It defines how the application fetches the content and the chapters from the targeted server.

[Here](EXAMPLE.md) an example how a fully configured server config looks like.

# 1. server
```json
{
    "server": "URL of Server"
}
```
Here you should write down the base URL to your target server. After the application start and the URL input from you the application checks if the string that is under the key `server` within the inputed URL.

# 2. request
```json
{
    "request": {
        "header": "httpRequestHeader",
        "coverHeader": "httpRequestHeader",
        "url": "urlToChapterlist",
        "filter": "getBook{Id}.html",
        "selfReferer": true,
        "coverSelfReferer": true
    }
}
```

The `header` key sets which httpHeader within the `configurations/header.json` should be used. If not set or not found the application uses the `default` header. The `coverHeader` is a optional argument and is used to give a differend header as parameter for the requests to the cover. If not set, it will be the same header as `header`. `coverHeader` can be usefull if the cover is on a differend server side and other arguments like `Host` for example are needed.

The `url` key is the url that is showing towards the external or internal server page where the chapter list is saved. The parameters for the current book will be added through the keys within `params`.

`filter` is used directly after the input of the target URL. It fetches the id of the book within the entered URL.
  
User input - `https://testHTML/niceBook.html`
```json
{
    "request": {
        "filter": "https://testHTML/{}.html"
    }
} 
```
The `{}` within the value of `filter` is where the ids of the book are normally(at the current server). So the application tries to delete everything around the id with the help of the `filter`. And the fetched id should be `niceBook`.

Request on - `https://testHTML/niceBook.html/chapter-1`
```json
{
    "request": {
        "selfReferer": true,
        "coverSelfReferer": true
    }
} 
```
Here is a differend case. The website needs a `Reference` that is dynamic to it's requests. So no static argument in `header.json` can be of use here. If you put here `selfReferer` and set it to `true` the web scraper sets the url of the website that is to visit in the `header` dynamicly every request. Like here: `Referer`: `https://testHTML/niceBook.html/chapter-1`. The `coverSelfReferer` is the same like `selfReferer` but for the session that is used for cover requests only. 

# 3. params
The part `params` is the most important 'cause it defines basicly what kind of server you want to fetch. Additionally it sets the parameters of the url that is used to get the chapter lists and more.

```json
{
    "params": {
        "type": true,
    }
}
```
Servers are divided into to kinds. Servers that are using externl chapter lists or servers that have their chapter lists at the same base page of the book that is targeted.

For external chapter lists you should set `type` to `true`. If internal than to `false`.

## <u> 3.1 External server </u>
```json
{
    "request": {
        "url": "https://testHTML/externalList",
        "filter": "https://testHTML{}.html"
    },
    "params": {
        "type": true,
        "id": "bookid",
        "add": "para=rw"
    }
}
```

The value of the key `id` sets the URL parameter key. The real key that is generated via the `filter` and the user input will be set under this URL key. So if the fetched book id is `niceBook` the parameter for the URL should look like this: `bookid=niceBook`.

The finished parameter will be added to the end of the value of the `url` key and the finished url towards the chapter list page should be like this.

`https://testHTML/externalList?bookid=niceBook`

The key `add` is only for available external servers. It is an optional parameter that will be also added to the end of the `url` value. The value of that key definies the parameter key and the value at the same time. So the parameter looks like this `para=rw`. 

`https://testHTML/externalList?bookid=niceBook&para=rw`

## <u> 3.2 Internal server </u>
```json
{
    "request": {
        "url": "https://testHTML/{}/externalList.html",
        "filter": "https://testHTML{}.html"
    },
    "params": {
        "type": false,
        "id": true
    }
}
```
Here is the key `id` that equals a bool value. If `id` is set to `true` the fetched book id `niceBook` will be entered into the value of the key `url` where the `{}` are.

`https://testHTML/niceBook/externalList.html`

## <u> 3.3 General keys </u>
### 3.3.1 More pages
If you set the key `page` the application is thinking the book has more than only one chapter list. So the application will continue fetching until no content is left where the pattern fits.

Here an example. The Value of `page` will be added to the end of the value of the key `url` within `request`. If set, the optional key `pageStart` defines which number is the first page. If not set the value of `pageStart` will default to `0`.
```json
{
    "request": {
        "url": "https://testURL{}.html"
    },
    "params": {
        "page": "?page=",
        "pageStart": 1
    }
}
```
So the finished generated url towards the chapter list should look like this:
```
https://testURL.html?page=1
https://testURL.html?page=2
https://testURL.html?page=3
...
```

# 4. Patterns of Content
Here is the configuration for the extraction of the content explained. For that it is to define the patterns for **chapterlist**, **chaptertitle** and **chaptercontnet**.

The **chapterlist** pattern is to fetch the known chapters out of the main page.  
**chaptertitle** and **chaptercontent** are used to get the content of the known chapters.

# 5 chaptertitle & chaptercontent
Fetching of the default content is mainly processed with the class `HTMLSearch`.

## <u> 5.1 Class - HTMLSearch </u>
This Class gets informations about the server configuration inside of `configurations/config.json` from the outside. This class makes the calls of `BeautifulSoup` easier, if the default pattern is needed.

For the common use the first method that is called **searchSection** is used. After that the method **searchElements** will be used.

The method **seachSection** sets the area and within this the method **searchElements** will fetch the content of the page.

### 5.1.1 Method - searchSection
**Only returns one result of the fetching process that should include the content.**  
This method sets the parent id or the class above the needed content. For that is used the function `b4s.find`. 'Cause of that it is required to address a unique class or id to go further in the fetching progess without problems. 

**<u>How to configure</u>**  
It's possible to use this function for the patterns `chapterlist`, `chaptertitle` and `chaptercontent`. You can set the class, id or both at the same time.

```json
    "chaptercontent": {
        "class": "sectionOfElements",
        "id": "sectionOfElements"
    }
```

### 5.1.2 Method - searchElements
**Returns a list of results that are compatible with the configured pattern.**  
This method searches within the area that is set with the method **searchSection**. If the method **searchSection** is not used this method will search through the whole web page. For that the method uses the function `b4s.find_all`. This returns a list of `b4s` objects. The content that is found will be seen within the finished EPUB.

**<u>How to configure</u>**  
It's possible to use this function for the patterns `chapterlist`, `chaptertitle` and `chaptercontent`. You can set the tag it's class and it's id in every combination.

```json
    "chaptercontent": {
        "tag": "Elements",
        "tagClass": "Elements",
        "tagId": "Elements"
    }
```

## <u> 5.2 Tag attributes </u>
Another key that is optional for the patterns `chaptertitle` and `chaptercontent` is `attribute`. This key is required if for example the content with the tag is not directly reachable 'cause of the attributes within the tag itself.

```json
    "chaptertitle": {
        "tag": "a",
        "attribute": "title"
    }
```

Here is the fetched tag element:
```html
<a href="linkToAnotherPage.html" title="Chapter 1">
```
And after the fetching using the pattern of the defined value `title` of the key `attribute` it should be look like this: `Chapter 1`.

# 6. chapterlist
This pattern is used to get the URL of the chapters that are known right out of the chapter list pages. 

The pattern of `chapterlist` is similar to the common patterns of `chaptertitle` and `chaptercontent`. The similarities of the named patterns are the keys `class`, `id`, `tag`, `tagClass`, `tagId` and `attribute`.

For the fetching of the URL links are only the common keys required. After that the additional keys `prefix` and `suffix` will be added to the fetched URLs if needed.

Fetched URLs fragmends to the known chapters:  
```
niceBook/chapter-1  
niceBook/chapter-2  
niceBook/chapter-3
niceBook/chapter-4
...
``` 

Here the configuration without the common keys.
```json
{
    "chapterlist": {
        "prefix": "https://testHTML/",
        "suffix": ".html"
    }
}
```

And after adding the prefix before and the suffix anfter the URL fragments it looks like this:
```
https://testHTML/niceBook/chapter-1.html  
https://testHTML/niceBook/chapter-2.html  
https://testHTML/niceBook/chapter-3.html  
https://testHTML/niceBook/chapter-4.html  
```