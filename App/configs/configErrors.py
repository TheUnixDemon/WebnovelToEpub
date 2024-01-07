def errorKeyNotFound(key: str):
    print("??? Key not found ???")
    print("The key '" + key + "' is not set")
    print("??? Key not found ???")

def errorWrongType(key: str, type: str):
    print("??? Wrong data type ???")
    print("The value of the key '" + key + "' has to be a '" + type + "'")
    print("??? Wrong data type ???")