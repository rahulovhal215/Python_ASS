import os
import sys
import hashlib

def checksum(Directory):
    Ret = os.path.exists(Directory)
    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(Directory)
    if Ret == False:
        print(f"{Directory} is not directory")
        return

    for FoldeName, SubFolderName, FileName in os.walk(Directory):
        for fname in FileName:
            filepath = os.path.join(FoldeName, fname)

            if os.path.isfile(filepath):
                fobj = open(filepath, "rb")
                data = fobj.read()
                fobj.close()

                hashobj = hashlib.md5(data)
                print(fname,"Checksum : ", hashobj.hexdigest())
def main():
    if (len(sys.argv)==1):
        print("Enter directory name")
        return
    checksum(sys.argv[1])

if __name__ == "__main__":
    main()
