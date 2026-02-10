import sys
import os

def LogDirectory(DirectoryName):
    if os.path.exists(DirectoryName) == False:
        print("There is no such directory")
        return
    
    if os.path.isdir(DirectoryName) == False:
        print(f"{DirectoryName} is not a directory")
        return

    FileDict = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            if fname in FileDict:
                FileDict[fname] +=1
            else:
                FileDict[fname] = 1

    fobj = open("Log.txt","w")

    for fname in FileDict:
        if FileDict[fname]>1:
            fobj.write(fname+"\n")
    fobj.close()
    print("Duplicate file names written in log.txt file")

def main():
    if (len(sys.argv)==1):
        print("Enter directory name")
        return
    LogDirectory(sys.argv[1])

if __name__ == "__main__":
    main()
