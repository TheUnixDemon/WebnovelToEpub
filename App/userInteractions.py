def printStart() -> None:
    print("")
    print("---- START ----")
    print("")


def printEnd() -> None:
    print("")
    print("---- DONE ----")
    print("")


def printNameError() -> bool:  # if a book with same name exists
    print("")
    print("---- THE BOOK EXISTS ALREADY ----")
    choice = input("Do you want to override the old book? (yes/no): ")
    print("")

    if choice == "yes" or choice == "y":
        return True

    else:
        return False


def printRequestError(URL: str, e: Exception) -> None:
    print("")
    print("<<<< ERROR >>>>")
    print("")
    print(f"Error > {URL}: {e}")
    print("")
    print("<<<< ERROR >>>>")
    print("")


def printTimeout() -> None:
    print("")
    print("---- TIMEOUT ----")
    print("")
    print("Program will wait for 45 secounds.")
    print("")


def printSkip() -> None:
    print("")
    print("---- URL SKIPPED ----")
    print("")


def printProgress(chapterURLs, currentURL) -> None:
    percent = ((currentURL + 1) / len(chapterURLs)) * 100
    print("Progress: " + str(percent) + " %")
