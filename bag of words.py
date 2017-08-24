import os
import sys

class plagarism():
        def __init__(self):
                self
        def dic(self,lst):                      #### Creating Dictionary for given file
                a={}
                lst1=open(lst,'r')
                lst1=lst1.read().split(' ')
                s = "@!#$%^&*()_+=|?+-`~';?.,:<>;"
                for j in s:
                        for i in range(0, len(lst1)):
                                lst1[i] = lst1[i].lower().replace(j," ")
                for i in range(len(lst1)):
                    if lst1[i] in a:
                        continue
                    else:
                        a[lst1[i]]=lst1.count(lst1[i])
                return a

        def dotproduct(self,s1,s2):              #Dot product of count of strings that are repeated
            sum=0
            for i in s1:
                if i in s2:
                    sum=sum+(s1[i]*s2[i])
            return sum


        def vectorproduct(self,s):            ####   ----> caluculating vector of given set of strings
            vec=0
            for i in s:
                vec=vec+(s[i]**2)
            norm=(vec)**(1/2)
            return norm
            

        def plagpercent(self,a,b):            ####  ---> Plagarism percentage caluculation   
                result=(a/b)*100
                return result
        
        def fileread(self):                     ## ---->Input of directory

                n=input("Enter the directory name: ")
                f=[]
                for i in os.listdir(n):
                    if i.endswith(".txt"):
                        f.append(i)
                os.chdir(n)
                lst3=[]
                lst4=[]
                for i in range(0, len(f)):
                    lst3.append(p.dic(f[i]))
                for i in range(len(f)):
                        for j in range(len(f)):
                                if(i==j):
                                     lst4.append(0)
                                else:
                                        f1=p.dotproduct(lst3[i],lst3[j])
                                        f2=p.vectorproduct(lst3[i])
                                        f3=p.vectorproduct(lst3[j])
                                        f4=f2*f3
                                        lst4.append(p.plagpercent(f1,f4))
                        print(lst4)
                        lst4=[]

p=plagarism()
p.fileread()
