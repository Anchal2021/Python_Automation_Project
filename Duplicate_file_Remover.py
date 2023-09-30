from sys import *
import os
import hashlib
import time


def Delefiles(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    icnt=0;

    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0

    else:
        print("NO duplicate files Found")

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()
def findDup(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirName,subdirs,filelist in os.walk(path):
            print("Current folder is:"+dirName)
            for filen in filelist:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Invalid Path")

def printresults(dict1):
    results=list(filter(lambda x:len(x)>1,dict.values()))

    if len(results)>0:
        print("duplicate Found")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No duplicate files found")

def main():
    print("-------code by Anchal-------")
    print("Application name:"+argv[0])

    if (len(argv)!=2):
        print("Error:Inavalid number of arguments")
        exit()

    if (argv[1]=="-h") or (argv[1]=="-H"):
        exit()

    if (argv[1]=="-u") or (argv[1]=="-U"):
        exit()

    try:
        arr={}
        startTime=time.time()
        arr=findDup(argv[1])
        printresults(arr)
        endTime=time.time()

        print("Took %s seconds to evaluate ."% (endTime-startTime))

    except ValueError:
        print("Error: Inavalid datatype of input")

    except Exception as E:
        print("Error :Invalid input",E)

if __name__=="__main__":
    main()





















