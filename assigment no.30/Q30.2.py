import sys
import os

def WordCount(FileName):
    Count = 0
    if os.path.exists(FileName):
        fobj = open(FileName,"r")
        for line in fobj:
            temp =""
            for ch in line:
                if ch!=" " and ch!="\n" and ch!= "\t":
                    temp += ch
                
                else:
                    if temp != "":
                        Count += 1
                        temp = ""
            if temp != "":
                Count += 1
        print("Number of words in file : ",Count)
        fobj.close()
        
    else:
        print("File not exist")

def main():
    if (len(sys.argv)==1):
        print("Enter file name")
        return
    WordCount(sys.argv[1])

if __name__ == "__main__":
    main()
