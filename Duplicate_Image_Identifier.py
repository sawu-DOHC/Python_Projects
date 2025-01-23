import os
import hashlib

#os.walk(top, topdown=True, onerror=None, followlinks=False)
#
#generates the file names in a directory tree by traversing either top down or bottom up.
#used to iterate through each directory and subdirectory starting from directoryPath, allowing the script to access each file within these directories.


#os.path.join(path, *paths)
#
#joins one or more path components to form a complete path.
#used to combine directory paths with filenames to create full file paths.

#os.path.basename(path)
#
#returns the base name of pathname path sripping out the directory path and returns only the filename.


#os.path.splitext(path)
#
#splits the path into a pair ( root, ext ) where ext is everything after the last period in the last pathname
#used to separate the file extension from the rest of the path


#hashlib.md5()
#
#creates a new hash object using the MD5 algorithm, which can be used to hash a block of data repeatedly.
#initializes a new MD5 hash object to compute a unique hash for each file.


#hash.update(data)
#
#updates the hash object with the bytes like object, which in this case, are chunks of the file being read.
#used inside a loop that reads the file in chunks; each chunk is used to update the hash.

#hash.hexdigest()
#
#returns the digest of the data passed to the update() method so far. This is a string object of double length, containing only hexadecimal digits.
#called after the entire file has been read and processed by the hash object to get the final hash value.




# paths for the source and destination directories
directoryPath = "C:/Users/Sam/OneDrive/Pictures Cloud/testfolder"
duplicatesFolder = "C:/Users/Sam/OneDrive/Pictures Cloud/testresultsfolder"

seenFiles = {}  # dictionary to store file hashes and their paths
duplicateFiles = []  # list to store paths of duplicate files

# function to calculate the md5 hash of a file
def calculate_md5( filePath ):

    hasher = hashlib.md5()  # create a new md5 hash object

    with open(filePath, 'rb') as file:  # open file in binary mode

        for chunk in iter(lambda: file.read(1024), b""):

            hasher.update( chunk )

    return hasher.hexdigest()  # return the complete hash of the file as a string of hexadecimal digits

# walk through each directory and subdirectory in the directory path
for currentDir, dirs, files in os.walk(directoryPath):

    # iterate through files in the current directory
    for file in files:

        # only process image files based on their extensions
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")):

            filePath = os.path.join(currentDir, file)  # construct full file path
            fileHash = calculate_md5(filePath)  # get md5 hash of the file

            # check if this file hash is already in the seenFiles dictionary

            if fileHash in seenFiles:
                print("duplicate found:", filePath, "matches", seenFiles[fileHash])  # report duplicate
                duplicateFiles.append(filePath)  # add duplicate file path to the list

            else:
                seenFiles[fileHash] = filePath  # store new file hash and path

# move all found duplicates to the duplicates folder
for filePath in duplicateFiles:

    fileName = os.path.basename(filePath)  # extract the file name from the file path
    destinationPath = os.path.join(duplicatesFolder, fileName)  # create destination path for the duplicate
    counter = 1

    # ensure no file name conflicts in the destination folder by appending a counter to the file name
    while os.path.exists(destinationPath):

        baseName, extension = os.path.splitext(fileName)  # split file name and extension
        destinationPath = os.path.join(duplicatesFolder, f"{baseName}_{counter}{extension}")  # append counter to file name
        counter += 1

    os.rename(filePath, destinationPath)  # move the file to the new location
    print("moved:", filePath, "to", destinationPath)  # print move operation details
