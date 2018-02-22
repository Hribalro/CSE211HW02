#Names
# Open file and get data with \n character stripped
def getFileLines(fileName):
    list = []
    
    for line in (open(fileName, "r")):
        list.append(line.rstrip("\n"))  # Delete trailing \n character

    return list

def loopThroughData():
    fileName = "Step1Data.txt"
    lines = getFileLines(fileName)
    lineIndex = 0
    
    # Run through each line of the supplied text file and check for each category of dictionary entry
    while (lineIndex < len(lines)):
        if (lines[lineIndex] == "Book"):
            createBook(lines[lineIndex + 1:lineIndex + 6])  # Pass all the necessary Book data to creator method
        
        lineIndex += 1

def createBook(bookInfo):
    print("Book found:")
    
    for x in bookInfo:
        print(": ", x)  # TO DO
        
    print("\n")

loopThroughData()