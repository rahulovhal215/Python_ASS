import sys
import os

def CopyFiles(Directory1,Directory2):
    Ret = os.path.exists(Directory1)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.exists(Directory2)
    if Ret == False:
        os.mkdir(Directory2)
    
    Ret = os.path.isdir(Directory1)
    if Ret == False:
        print(f"{Directory1} it not directory.")
        return

    Ret = os.path.isdir(Directory2)
    if Ret == False:
        print(f"{Directory2} it not directory.")
        return

    for FolderName, SubFolderName, FileName in os.walk(Directory1):
        for fname in FileName:
            sourcepath = os.path.join(FolderName, fname)
            destpath = os.path.join(Directory2,fname)

            if os.path.isfile(sourcepath):
                fsource = open(sourcepath,"rb")
                fdest = open(destpath,"wb")

                data = fsource.read()
                fdest.write(data)

                fsource.close()
                fdest.close()

    print("Directory files copied successfully")
            
def main():
    if (len(sys.argv)<3):
        print("Enter two directory name")
        return
    CopyFiles(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
