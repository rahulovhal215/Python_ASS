import sys
import os

def LineCount(FileName):
    Count = 0
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        for line in fobj:
            Count += 1
        print("Number of line : ",Count)
        fobj.close()
        
    else:
        print("File not exist")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    LineCount(sys.argv[1])

if __name__ == "__main__":
    main()