import sys
import os

def word(FileName):
    inp = (input("Enter word : "))

    if os.path.exists(FileName):
        fobj = open(FileName)
        data = fobj.read()

        if inp in data:
            print(f"{inp} is present in {FileName}")
        else:
            print(f"{inp} is not present in {FileName}")
        fobj.close()

def main():
    if (len(sys.argv) == 1):
        print("Enter file name please")
        return
    word(sys.argv[1])

if __name__ == "__main__":
    main()