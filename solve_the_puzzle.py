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

def rename_files() :
    prank_home = os.getcwd()+"\\resources\\prank"
    print(prank_home)

    os.chdir(prank_home)

    for dirpath,dirnames,filenames in os.walk(prank_home) :
        #it yields a 3-tuple list (dirpath, dirnames, filenames).
        #it literally walks down the tree, one at a time,so this is O(n) in time complexity
        for file in filenames :
            new_name = ""
            for character in file :
                if not character.isdigit():
                    new_name = new_name + character
                    #TODO : there is no need to parse the file extension. It's an additional step
            #new_name = new_name + file[file.find("."):]
            print ("renaming ", file , " to :", new_name)
            #!os.rename only operates on current working directory, you can't set an absolute path in the src/dst input params
            os.rename(file,new_name)
#
# def rename_files_2() :
#     #!os.listdir returns every thing in directory, regardless of type
#     #!starting a string with r means to interpret string as raw
#     file_list = os.listdir(os.getcwd()+ r"\resources\prank")
#     print (file_list)
#
#     #!before you start writing code from scratch, always look to see if the library already provides that functionality
#     #!library functions are usually optimized and it is best to use those rather than write your own code from scratch
#
#     for file_name in file_list :
#         #string.translate(table of character conversion mapping, characters to be removed)
#         #i don't know if this is still valid in python 3.0?
#         new_name = file_name.translate("0123456789")
#         print (file_name , " :: ", file_name.translate(None,b'0123456789'))
#

print ("start program")
rename_files()
