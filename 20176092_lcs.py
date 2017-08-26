import os, re

class lcs(object):                       ####Converting file into list of words
  def __init__(self, f):
    self.f = f
    self.file=open(f,"r")
    self.s=[]
    for i in self.file:
      for j in re.findall(r"\w+", i):
        j = j.lower()
        self.s.append(j)
    
    
  def compare(self,l1,l2):                ####Comparing two files and finding lcs
    lcs=0
    k = []
    for i in range(len(l1)):
      x=i
      y=x
      for j in range(len(l2)):
        if(x<len(l1)):
          if(l1[x]==l2[j]):
            x=x+1
            if(x-i)>lcs:
              lcs=x-i
              k=l1[i:x]
          else:
            x=y
    k = ' '.join(k)
    l1 = ' '.join(l1)
    l2 = ' '.join(l2)
    print(k)
    return(len(k) * 2/(len(l1) + len(l2)))*100
  
n=input("Enter the directory name: ")             ####    Taking input of files
os.chdir(n)
files = []
for i in os.listdir(n):
  if i.endswith(".txt"):
    o = lcs(i)
    files.append(o)
l = []
for i in range(0, len(files)):                    ####    Calling "Compare" function
  for j in range(0,len(files)):
    if i == j:
      l.append(0)
    else:
      l.append(files[j].compare(files[j].s,files[i].s))
for i in range(len(files)):
  print("\t",files[i].f,end=" ")
for i in range(len(files)):
  print("\n", files[i].f,l)
