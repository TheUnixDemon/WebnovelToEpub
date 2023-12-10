def printStart():
    print("")
    print("---- START ----")
    print("")

def printEnd():
    print("")
    print("---- DONE ----")
    print("")
    
def printNameError(): # if a book with same name exists
    print("")
    print("---- THE BOOK EXISTS ALREADY ----")
    choice = input("Do you want to override the old book? (yes/no): ")
    print("")
    
    if(choice == "yes" or choice == "y"):
        return True
    
    else:
        return False

def printRequestError(URL, e):
    print("")
    print("<<<< ERROR >>>>")
    print("")
    print(f"Error > {URL}: {e}")
    print("")
    print("<<<< ERROR >>>>")
    print("")
    
def printTimeout():
    print("")
    print("---- TIMEOUT ----")
    print("")
    print("Program will wait for 45 secounds.")
    print("")
    
def printSkip():
    print("")
    print("---- URL SKIPPED ----")
    print("")

def printProgress(chapterURLs, currentURL):
    percent = ((currentURL + 1) / len(chapterURLs)) * 100
    print("Progress: " + str(percent) + " %")