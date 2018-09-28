#The Problem :
# rename files in "Prank" folder by removing all digits in the file name
#*****************************************************************************

#The Solution :
# read list of file names from folder
# while exists file in list :
    # read each character in filename
    # if character is a digit remove from string
    # rename file to new string

# advanced programming questions:
# what is the time and space complexity order of this code?
# what are some of the edge cases of the question?

import os

prank_home = os.getcwd()+"\\resources\\prank"
print(prank_home)

for dirpath,dirnames,filenames in os.walk(prank_home) :
    #it yields a 3-tuple list (dirpath, dirnames, filenames).
    #it literally walks down the tree, one at a time,so this is O(n) in time complexity
    for file in filenames :
        new_name = ""
        for character in file :
            if not character.isdigit():
                new_name = new_name + character
            elif character == ".":
                break
        #keep the file extension
        #new_name = new_name + file[file.find("."):]
        print ("renaming ", file , " to :", new_name)
        #os.rename(file,new_name)
