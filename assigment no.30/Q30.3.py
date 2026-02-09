import sys
import os
import time 

def Content(FileName):
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        print("Contents of the file is: \n")
        for data in fobj:
            print(data)
            time.sleep(0.05)
        fobj.close()
    else:
        print("There is no such file")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    Content(sys.argv[1])
        
if __name__=="__main__":
    main()

