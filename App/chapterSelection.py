
def selectChapters(chapterURLs: list[str]) -> list[str]: # is used after of fetching urls
    firstChapter: int = 1
    lastChapter: int = len(chapterURLs)

    print("--- Known chapters ---")
    if len(chapterURLs) > 300: # to much entries
        lastNumber = str(len(chapterURLs)) + ": "
        print(str(firstChapter) + ": " + chapterURLs[0] + " ... " + str(lastChapter) + ": " + chapterURLs[-1])
    else:
        chapterNumber: int = 1 # counter for chapters
        for chapterURL in chapterURLs:
            print(str(chapterNumber) + ": " + chapterURL)
            chapterNumber += 1
            
    while True:
        print("--- Chapter selection ---")
        while True:
            try:        
                chapterStart: str = input("Enter first chapter: ")
                chapterEnd: str = input("Enter last chapter: ")
                
                # checks if something is entered
                if not chapterStart or not chapterEnd: # convert str into int
                    raise Exception("Input cannot be empty")
                
                # checks if a number is entered
                chapterStart = int(chapterStart)
                chapterEnd = int(chapterEnd)
                    
                # checks if numbers are in range
                rangeError: str = "Entered chapter numbers has to be in range of " + str(firstChapter) + " and " + str(lastChapter)
                if chapterStart < firstChapter or chapterStart > lastChapter:
                    raise Exception(rangeError)
                if chapterEnd < firstChapter or chapterEnd > lastChapter:
                    raise Exception(rangeError)
                
                if chapterStart > chapterEnd:
                    raise Exception("Entered first chapter has to be smaller or equal to the last entered chapter.")
            except ValueError:
                print("Error: Input has to be a number")
            except Exception as e:
                print("Error:", e)
            else: # no errors happened
                break

        print("--- selected chapters ---")
        print(str(firstChapter) + ": " + chapterURLs[chapterStart - 1] + " ... " + str(len(chapterURLs[chapterStart - 1:chapterEnd])) + ": " + chapterURLs[chapterEnd - 1])
        while True:
            try:
                answer: str = input("Are those the selected chapters that you want? (y/n): ").lower()
                if answer not in ["y", "n"]:
                    raise ValueError("Non valid answer. Please enter only 'n' or 'y'")
            except ValueError as e:
                print("Error:", e)
            else: # returns selected chapters
                if answer == "n":
                    break
                selectedChapterURLs: list[str] = chapterURLs[chapterStart - 1:chapterEnd]
                return selectedChapterURLs