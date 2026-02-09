import os
import sys

def CopyData(FileName1,FileName2):
    if os.path.exists(FileName1):
        fobj = open(FileName1,"r")
        data = fobj.read()
        
        dobj = open(FileName2,"w")
        dobj.write(data)

        fobj.close()
        dobj.close()

        print(f"Contents of {FileName1} copied into {FileName2}")
    else :
        print("File not exists")
def main():
    if (len(sys.argv)!=3):
        print("Please enter two filename")
        return
    
    CopyData(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()

