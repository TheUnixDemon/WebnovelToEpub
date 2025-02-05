from bs4 import BeautifulSoup

class HTMLSearch:     
    def setSoup(self, soup: BeautifulSoup) -> None: # for soup changing after object creation
        self.__soup = soup
    
    def getSoup(self) -> BeautifulSoup:
        return self.__soup
    
    def returnSoup(self):
        if not self.__soup:
            print("<< B4SError: Soup is empty or not set >>")
        elif isinstance(self.__soup, list):
            for element in self.__soup:
                print(element.prettify())
        else:
            print(self.__soup.prettify())
        
    # searches elements and creates a soup list
    def searchElements(self, tagHtml: str = None, classHtml: str = None, idHtml: str = None):
        localSoup: BeautifulSoup = self.__soup
        # tags are required
        if classHtml or idHtml:
            if classHtml and idHtml:
                elementsSoup = localSoup.find_all(tagHtml, class_=classHtml, idHtml=idHtml)
            else:
                if classHtml:
                    elementsSoup = localSoup.find_all(tagHtml, class_=classHtml)
                elif idHtml:
                    elementsSoup = localSoup.find_all(tagHtml, id=idHtml)
        else:
            elementsSoup = localSoup.find_all(tagHtml)

        self.setSoup(elementsSoup)
            
    # creates a section as a hole soup element
    def searchSection(self, classHtml: str = None, idHtml: str = None): # classes and/or ids
        localSoup: BeautifulSoup = self.__soup
        if classHtml and idHtml:
            sectionSoup = localSoup.find(class_=classHtml, id=idHtml)
        else:
            if classHtml:
                sectionSoup = localSoup.find(class_=classHtml)
            elif idHtml:
                sectionSoup = localSoup.find(id=idHtml)
                
        self.setSoup(sectionSoup)