import sys
import os

def Extension(directory, Extension):
    Ret = os.path.exists(directory)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(directory)
    if Ret == False:
        print("It is not a directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(directory):
        for fname in FileName:
            if fname.endswith(Extension):
                print("File name : ",os.path.join(FolderName, fname))


def main():
    if (len(sys.argv)==1):
        print("Enter directory name")
        return
    Ext = input("Enter file estension : ")
    Extension(sys.argv[1],Ext)

if __name__=="__main__":
    main()