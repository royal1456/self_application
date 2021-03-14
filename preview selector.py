#a simple program to copy duplicates/high resolution as per  original/low ones in a directory (uses file number to match them)
import os
import shutil
flag=0
log=[]
loc=input('preview  location:') #takes location of preview(low resoslution files)
org=input('original  location:') #takes location of original(high resoslution files)
fol=input('save folder location:') #takes location of path or folder to saved

def write(loc):
    try:
        file =open(os.path.join(loc,"uncopied.txt"),'w')
        file.write("\n".join(log))
        file.close()
        print("Written")
    except:
        print("Unable to write try giving another path to write text file \n or write exit to exit")
        new_loc=input()
        if(new_loc!="exit"):
            write(new_loc)

orgl=os.listdir(org)
locl = os.listdir(loc)
foll = os.listdir(fol)
for i in locl:
    try:
        new=os.path.join(org,i)
        shutil.copy(new, fol)
    except:
        flag=1
        log.append(i)
        
if(flag==0):
    print("ALL Preview files read and copied  prss an key to exit")
    p=input()
else:
    print("All files are not copied\n",*log,sep=",")
    print("Write copyto write their names in file in save  folder  or type exit")
    while(1):
        inp=input()
        if(inp=="copy"):
            write(fol)
            print("press any key to exit")
            input()
            break
        elif(inp=="exit"):
            break
        print("make sure your spelling are correct copy,no caps")
        
