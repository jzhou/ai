import os,sys
import time

def writefile():
    myfile = open("./myfile.txt","a",0)
    myfile.write("content1")
    print ("see changes on myfile")
    time.sleep(10)
    myfile.write("content2")
    print ("see changes on myfile")

def writefile2():
    myfile = open("./myfile.txt","a")
    myfile.write("content1")
    print ("see changes on myfile")
    time.sleep(10)
    myfile.write("content2") #write to program buffer
    print ("see changes on myfile")
    myfile.flush()    #write to os buffer
    os.fsync(myfile) #write to  disk

def print_help():
    msg="""
    file.py [1|2]
    """


if __name__=="__main__":
    if "1" in sys.argv[1:]:
        writefile()
    elif "2" in sys.argv[1:]:
        writefile2()
    else:
        print_help()
      

