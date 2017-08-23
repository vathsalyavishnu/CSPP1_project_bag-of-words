import os
import sys

def dic(lst):
        a={}
        l=[]
        lst1=open(lst,'r')
        lst1=lst1.read().split(' ')
        for i in range(0, len(lst1)):
                lst1[i] = lst1[i].lower().replace("."," ").replace("\n","").replace(",","")
        for i in range(len(lst1)):
            if lst1[i] in a:
                continue
            else:
                a[lst1[i]]=lst1.count(lst1[i])
        return a

def dotproduct(s1,s2):
    sum=0
    for i in s1:
        if i in s2:
            sum=sum+(s1[i]*s2[i])
    return sum


def vectorproduct(s):
    vec=0
    for i in s:
        vec=vec+(s[i]**2)
    norm=(vec)**(1/2)
    return norm
    

def plagpercent(a,b):
        result=(a/b)*100
        return result

n=input("Enter the directory name: ")
f=[]
for i in os.listdir(n):
    if i.endswith(".txt"):
        f.append(i)
os.chdir(n)
lst3=[]
lst4=[]
for i in range(len(f)):
        for j in range(len(f)):
                if(i==j):
                     lst4.append(0)
                else:
                        lst3.append(dic(f[i]))
                        print(lst3)
                        lst3.append(dic(f[j]))
                        f1=dotproduct(lst3[i],lst3[j])
                        f2=vectorproduct(lst3[i])
                        f3=vectorproduct(lst3[j])
                        f4=f2*f3
                        lst4.append(plagpercent(f1,f4))
        print(lst4)
        lst4=[]
