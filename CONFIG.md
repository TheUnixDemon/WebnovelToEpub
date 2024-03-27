# Configurations
Every configuration file lays within the folder `configurations/`. 

# config.json
`config.json` is for server based configuration. It defines how the application fetches the content and the chapters from the targeted server.

```json
[
    {
        "server": "ServerURL", // example: http://google.de/
        "request": {
            "header": "httpRequestHeader", // look at the `header.json`
            "url": "urlToChapterlist",
            "filter": "getBook{Id}.html", // should remove all around the id of the chosen book
            "pattern": {
                "chapterlist": {
                    "urlPattern": "/urlPart/",
                    // find() -> class & id defines the section, has to be unique
                    "class": "sectionOfElements",
                    "id": "sectionOfElements",
                    // find_all() -> <tag class=class id=id>content</tag> 
                    "tag": "Elements",
                    "tagClass": "Elements",
                    "tagId": "Elements",
                    // prefix & suffix will be added to "content"
                    "prefix": "addsAtTheBeginning",
                    "suffix": "addsAtTheEnd",
                    "attribute": "attributeOfElements"
                },
                "chaptertitle": {
                    "class": "sectionOfElements",
                    "id": "sectionOfElements",
                    // find_all() -> <tag class=class id=id>content</tag> 
                    "tag": "Elements",
                    "tagClass": "Elements",
                    "tagId": "Elements",
                    "attribute": "attributeOfElements"
                },
                "chaptercontent": {
                    "class": "sectionOfElements",
                    "id": "sectionOfElements",
                    // find_all() -> <tag class=class id=id>content</tag> 
                    "tag": "Elements",
                    "tagClass": "Elements",
                    "tagId": "Elements",
                    "attribute": "attributeOfElements"                    
                }
            },
            "params": { // only releated to "chapterlist", "url" & "filter"
                "type": true, // external or internal chapter lists
                "id": "key", // id parameter key url?key=id
                "page": "pageKey", // if chapter list are more than one
                "add": "additionalStaticParameters",
            }
        }
    }
]
```

# header.json
`header.json` is the request header that is mostly required by the servers.

# schema.json
`schema.json` sets rules for a required structure of the jsons that was named before. The applications checks these rules at the beginning.