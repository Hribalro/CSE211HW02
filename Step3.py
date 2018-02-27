'''
Steven Sitko, Ryan Hribal, Peter something lol, Lucas Agin
CSE211 - Homework#2
Python version 3.6
'''

# Open file and get data with \n character stripped
def getFileLines(fileName):
    list = []
    
    for line in (open(fileName, "r")):
        list.append(line.rstrip("\n"))  # Delete trailing \n character

    return list

# ################# #
# String operations #
# ################# #

# Get the key of a line prefixed with "Key: "
def getKey(line):
    key = line.split(": ")[1]
    return key

# Remove prefixes on info like "Author: "
def removePrefix(string):
    return string.split(": ")[1]

# ##################### #
# Dictionary operations #
# ##################### #

# Run through all data and add each item to a dictionary
def createDictionary():
    fileName = "Step3Data.txt"
    lines = getFileLines(fileName)
    lineIndex = 0
    dict = {}

    # Run through each line of the supplied text file and check for each category of dictionary entry
    while lineIndex < len(lines):
        if lines[lineIndex] == "Book":
            key = getKey(
                lines[lineIndex + 1])  # Key for accessing the Book data created by createBook(), stored in dictionary
            value = createBook(lines[lineIndex + 2:lineIndex + 6])  # Pass all the necessary Book data to creator method
            dict[key] = value
        elif lines[lineIndex] == "Journal":
            key = getKey(lines[lineIndex + 1])
            value = createJournal(lines[lineIndex + 2:lineIndex + 9])
            dict[key] = value
        elif lines[lineIndex] == "Conference":
            key = getKey(lines[lineIndex + 1])
            value = createConference(lines[lineIndex + 2:lineIndex + 8])
            dict[key] = value
            
        lineIndex += 1

    return dict

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

def createJournal(journalInfo):
    finalString = ""
    
    # Add author name in order of last, first
    authorLastFirst = removePrefix(journalInfo[0]).split(" ")
    finalString += authorLastFirst[1] + ", " + authorLastFirst[0] + ", "
    
    # Add title
    title = removePrefix(journalInfo[1])
    finalString += title + ", "
    
    # Add journal
    journalTitle = removePrefix(journalInfo[2])
    finalString += journalTitle + ", "
    
    # Add publisher
    publisher = removePrefix(journalInfo[3])
    finalString += publisher + ":"

    # Add volume
    volume = removePrefix(journalInfo[5])
    finalString += volume
    
    #Add number
    number = removePrefix(journalInfo[6])
    finalString += "(" + number + "), "
        
    # Add date
    date = removePrefix(journalInfo[4])
    finalString += date + "."
    
    return finalString

def createConference(conferenceInfo):
    finalString = ""
    
    # Add author name in order of last, first
    authorLastFirst = removePrefix(conferenceInfo[0]).split(" ")
    finalString += authorLastFirst[1] + ", " + authorLastFirst[0] + ", "
    
    # Add title
    title = removePrefix(conferenceInfo[1])
    finalString += title + ", in Proceedings of "
    
    # Add conference
    conference = removePrefix(conferenceInfo[2])
    finalString += conference + ", "
    
    #Add location
    location = removePrefix(conferenceInfo[4])
    finalString += location + ", "
    
    #Add date
    date = removePrefix(conferenceInfo[3])
    date = date.replace(".", ", ")
    finalString += date
    
    #Add pages
    pages = removePrefix(conferenceInfo[5])
    pages = pages.replace(" ", "")
    finalString += pages + "."
    
    return finalString

# ########## #
# User input #
# ########## #

def getInput(msg):
    return input(msg)

# ############### #
# Executable code #
# ############### #

dictionary = createDictionary()
print(dictionary)
choice = str()

while choice != "exit":
    choice = getInput("Please enter dictionary search key.  Type \"exit\" to quit: ")
    if choice in dictionary:
        print(choice, "\t", dictionary[choice], "\n ")
    elif choice == "exit":
        break
    else:
        print("No such key in dictionary\n")
