import os
import sys
import math

def dic(lst):
	a={}
	for i in range(len(lst)):
		a[lst[i]]=lst.count(lst[i])
	return a
      
def dotproduct(s1,s2):
	sum=0
	for i in s1:
		if i in s2:
			sum=sum+(s1.get(i)*s2.get(i))
	return sum

def vectorproduct(s):
	vec=0
	for i in s:
		vec=vec+(s.get(i)**2)
	norm=(vec)**(1/2)
	return norm


lst1=open("1.txt",'r')
lst1=lst1.read().split(' ')
s1=dic(lst1)

lst2=open("2.txt","r")
lst2=lst2.read().split(" ")
s2=dic(lst2)

v1=vectorproduct(s1)
v2=vectorproduct(s2)

num=dotproduct(s1,s2)
denom=v1*v2

result=(num/(denom))*100
print("plagarism = ",result,"%")
