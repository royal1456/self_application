#a simple program to copy high resolution as per  low ones in a directory (uses file number to match them)
import os
import shutil
def copy(add,org):
    new=org+"\\"+add
    return(new)

loc=input('preview ki location:')#takes location of preview(low resoslution files)
org=input('original ki location:')#takes location of original(high resoslution files)
fol=input('save krne vale folder ki location:')#takes location of path or folder to saved

size=len(os.listdir(loc))
pos = len(os.listdir(org))
orgl=os.listdir(org)
locl = os.listdir(loc)
foll = os.listdir(fol)
os.chdir(fol)
for i in range(size):
   for j in range(pos):
        if (locl[i]==orgl[j]):
             new=copy(locl[i],org)

             shutil.copy(new, fol)
             break


p=input()

