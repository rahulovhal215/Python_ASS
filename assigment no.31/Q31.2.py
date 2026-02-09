import sys
import os

def Rename(DirName,Ext1,Ext2):
    Ret = False
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if Ret == False:
        print(f"{DirName} is not Directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            if fname.endswith(Ext1):
                old_path = os.path.join(FolderName,fname)

                new_name = fname.replace(Ext1,Ext2)
                new_path = os.path.join(FolderName, new_name)

                os.rename(old_path, new_path)
                print("Renamed : ",fname, "-",new_name)

def the():
    if (len(sys.argv)==1):
        print("Enter Directory Name : ")
        return
    
    Ext1 = input("Enter first file extension : ")
    Ext2 = input("Enter secont file extension : ")

    Rename(sys.argv[1],Ext1,Ext2)

def main():
    the()
if __name__ == "__main__":
    main()

