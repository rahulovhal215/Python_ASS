import sys
import os
import hashlib
import time

def DirectoryScanner(DirName):

    if not os.path.exists(DirName):
        print("There is no such directory")
        return

    if not os.path.isdir(DirName):
        print("It is not a directory")
        return

    fobj = open("Log.txt", "w")

    FileDict = {}
    TotalFiles = 0
    DuplicateCount = 0

    for FolderName, SubFolder, FileNames in os.walk(DirName):
        for fname in FileNames:
            TotalFiles += 1
            FilePath = os.path.join(FolderName, fname)

            hobj = hashlib.md5()
            f = open(FilePath, "rb")
            hobj.update(f.read())
            f.close()

            FileHash = hobj.hexdigest()

            if FileHash in FileDict:
                fobj.write("Duplicate file deleted : " + FilePath + "\n")
                os.remove(FilePath)
                DuplicateCount += 1
            else:
                FileDict[FileHash] = FilePath

    fobj.write("\nTotal files scanned : " + str(TotalFiles) + "\n")
    fobj.write("Total duplicate files deleted : " + str(DuplicateCount) + "\n")
    fobj.close()


def main():
    if len(sys.argv) != 2:
        print("Directory name please")
        return

    StartTime = time.time()
    DirectoryScanner(sys.argv[1])
    EndTime = time.time()

    print("Time required : ",EndTime-StartTime,"seconds")
if __name__ == "__main__":
    main()