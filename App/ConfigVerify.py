import json
from jsonschema import validate

from LoadJson import LoadJson

class ConfigVerify(LoadJson):
    def __init__(self):
        super().__init__()
        self.__config: json = super().getConfig()
        self.__httpHeader: json = super().getHttpHeader()
        self.__defaultHttpHeader: json = self.__httpHeader.get("default", None)
        
        # loads configured requirements of config
        schema: json = super().loadJsonFile("schema.json")
        self.__schemaConfig: json = schema.get("config", None)
        self.__schemaDefaultHttpHeader: json = schema.get("defaultHttpHeader", None)

    def Config(self) -> None:
        try:
            validate(instance=self.__config, schema=self.__schemaConfig)
        except Exception as e:
            print(f"<< 'config.json' fullfills not the requirements {e}>>")
            exit()

    def defaultHttpHeader(self) -> None:
        try:
            validate(instance=self.__defaultHttpHeader, schema=self.__schemaDefaultHttpHeader)
        except Exception as e:
            print(f"<< 'header.json' fullfills not the requirements: {e}>>")
            exit()