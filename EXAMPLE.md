# 1. Server configuration

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