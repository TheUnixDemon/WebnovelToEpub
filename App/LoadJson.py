import json

class LoadJson:
    def __init__(self):
        self.__config: json = self.loadJsonFile("config.json")
        self.__httpHeader: json = self.loadJsonFile("header.json")

    def loadJsonFile(self, jsonFileName: str) -> json: # loads and returns json data
        try:
            with open("configurations/" + jsonFileName, "r") as f:
                jsonFile: json = json.load(f)
                return jsonFile
        except FileNotFoundError:
            print(f"<< Error: File '{jsonFileName}' not found. >>")
        except json.JSONDecodeError as e:
            print(f"<< Error: loading JSON configuration from '{jsonFileName}': {e} >>")
            
    def getConfig(self) -> json:
        return self.__config
    
    def getHttpHeader(self) -> json:
        return self.__httpHeader