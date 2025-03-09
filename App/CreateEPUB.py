from ebooklib import epub
import requests

class CreateEPUB:
    def __init__(self, bookTitle: str, bookFilename: str, bookAuthor: str):
        # part of book structure
        self.__ebook = epub.EpubBook()
        self.__ebook.spine = ["nav"]
        self.__ebook.toc = []
        # metadata
        self.__bookTitle = bookTitle
        self.__bookAuthor = bookAuthor
        self.__bookLanguage = "en"
        self.__bookFilename = bookFilename
        self.__xhtmlFileNumber: int = 1 # for valid file names
        self.addMetadata() # adds metadata to the book
            
    def addMetadata(self) -> None:
        self.__ebook.set_title(self.__bookTitle)
        self.__ebook.set_language(self.__bookLanguage)
        self.__ebook.add_author(self.__bookAuthor)        
        
    def addChapter(self, chapterTitle: str, chapterContent: list[str]) -> None:
        # sets filename for current chapter
        xhtmlFilename: str = "file" + str(self.__xhtmlFileNumber) + ".xhtml"
        self.__xhtmlFileNumber += 1
        # adds new chapter
        currentChapter: epub = epub.EpubHtml( # adds metadata for current chapter
            title = chapterTitle,
            file_name = xhtmlFilename,
            lang = self.__bookLanguage
            )
        titleHTML = "<h1 id='chapter'>" + chapterTitle + "</h1>"
        #contentHTML = "\n".join(["<p>{}</p>".format(item) for item in chapterContent]) # adds p tags and make a hole string out of this list
        contentHTML = "\n".join(chapterContent)
        currentChapter.set_content(titleHTML + "\n" + contentHTML) # sets content to current chapter
        self.__ebook.add_item(currentChapter) # adds current chapter to the book
        self.__ebook.toc.append(epub.Link(xhtmlFilename, chapterTitle, "chapter"))
        self.__ebook.spine.append(currentChapter)
        
    def addCover(self, coverImage: requests.Response) -> None:
        self.__ebook.set_cover("cover.png", coverImage.content)

    def writeBook(self) -> None:
        self.__ebook.add_item(epub.EpubNcx())
        self.__ebook.add_item(epub.EpubNav())
        epub.write_epub(self.__bookFilename, self.__ebook)