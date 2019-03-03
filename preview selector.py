import os
import shutil
def copy(add,org):
    new=org+"\\"+add
    return(new)

loc=input('preview ki location:')
org=input('original ki location:')
fol=input('save krne vale folder ki location:')

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

