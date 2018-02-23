# Open file and get data with \n character stripped
def getFileLines(fileName):
    list = []
    
    for line in (open(fileName, "r")):
        list.append(line.rstrip("\n"))  # Delete trailing \n character

    return list

# Get the key of a line prefixed with "Key: "
def getKey(line):
    key = line.split(": ")[1]
    return key

# Run through all data and add each item to a dictionary
def createDictionary():
    fileName = "Step1Data.txt"
    lines = getFileLines(fileName)
    lineIndex = 0
    dict = {}
    
    # Run through each line of the supplied text file and check for each category of dictionary entry
    while (lineIndex < len(lines)):
        if (lines[lineIndex] == "Book"):
            key = getKey(lines[lineIndex + 1])                      # Key for accessing the Book data created by createBook(), stored in dictionary
            value = createBook(lines[lineIndex + 2:lineIndex + 6])  # Pass all the necessary Book data to creator method
            dict[key] = value
        
        lineIndex += 1

    return dict

# Remove prefixes on info like "Author: "
def removePrefix(string):
    return string.split(": ")[1]

# Given 4 lines of info, create a properly formatted Book entry for the dictionary
def createBook(bookInfo):
    finalString = ""
    
    # Add author name in order of first, last
    authorFirstLast = removePrefix(bookInfo[0]).split(" ")
    finalString += authorFirstLast[1] + ", " + authorFirstLast[0] + ", "
    
    # Add book title
    bookTitle = removePrefix(bookInfo[1])
    finalString += bookTitle + ", "
    
    # Add publisher
    publisher = removePrefix(bookInfo[2])
    finalString += publisher + ", "
    
    # Add date
    date = removePrefix(bookInfo[3])
    finalString += date + "."
    
    return finalString

dictionary = createDictionary()
print(dictionary["Rowling1997"])