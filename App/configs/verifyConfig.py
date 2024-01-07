import sys
import json
import re

import configErrors

def requiredEntries(serverConfig: json) -> bool:
    status = True
    commonKeys = ["server", "request"]
    requestKeys = ["method", "url", "pattern", "params"]
    patternKeys = ["chaptertitle"]
    chaptertitleKeys = ["class", "tag"]
    
    for commonKey in commonKeys:
        if commonKey in serverConfig: # checks if the needed key is included
            value = serverConfig[commonKey]
            match commonKey:
                case "server":
                    if not type(value) is str:
                        configErrors.errorWrongType(commonKey, "String")
                        status = False
                case "request":
                    if not type(value) is dict:
                        configErrors.errorWrongType(commonKey, "Dictionary")
                        status = False
        else:
            configErrors.errorKeyNotFound(commonKey)        
            status = False
    
    if status:
        for requestKey in requestKeys:
            if requestKey in serverConfig["request"]:
                value = serverConfig["request"][requestKey]
                match requestKey:
                    case "method":
                        if not type(value) is str:
                            configErrors.errorWrongType(requestKey, "String")
                            status = False
                    case "url":
                        if not type(value) is str:
                            configErrors.errorWrongType(requestKey, "String")
                            status = False
                    case "pattern":
                        if not type(value) is dict:
                            configErrors.errorWrongType(requestKey, "Dictionary")
                            status = False
                    case "params":
                        if not type(value) is dict:
                            configErrors.errorWrongType(requestKey, "Dictionary")
                            status = False
            else:
                configErrors.errorKeyNotFound(requestKey)        
                status = False
    if status:
        for patternKey in patternKeys:
            if patternKey in serverConfig["request"]["pattern"]:
                value = serverConfig["request"]["pattern"][patternKey]
                match patternKey:
                    case "chaptertitle":
                        if not type(value) is dict:
                            configErrors.errorWrongType(patternKey, "Dictionary")
                            status = False
            else:
                configErrors.errorKeyNotFound(patternKey)        
                status = False
    if status:
        for chaptertitleKey in chaptertitleKeys:
            if chaptertitleKey in serverConfig["request"]["pattern"]["chaptertitle"]:
                value = serverConfig["request"]["pattern"]["chaptertitle"][chaptertitleKey]
                match chaptertitleKey:
                    case "class":
                        if not type(value) is str:
                            configErrors.errorWrongType(chaptertitleKey, "String")
                    case "tag":
                        if not type(value) is str:
                            configErrors.errorWrongType(chaptertitleKey, "String")
                            status = False
            else:
                configErrors.errorKeyNotFound(chaptertitleKey)        
                status = False
                
    return status
            
# checks the server spezific configuration
def verifyServerConfig(serverConfig: json) -> bool:
    status = requiredEntries(serverConfig)
    if status is False:
        sys.exit()