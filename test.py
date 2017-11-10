#! /usr/bin/python
# -*- coding:UTF-8 -*-
'''
num=input("please input your num:")
num=int(num)
for i in range(1,num):
	sumyinshu=0
	for yinshu in range(1,i):
		if num % yinshu  == 0:
				sumyinshu=sumyinshu+yinshu
	if sumyinshu==i:
		print(i,"is perfect!")
	elif(sumyinshu<i):
		print(i,"is abundant!")
	elif(sumyinshu>i):
		print(i,"is deficient!")
'''
'''
import yaml
temp_h = open('temp.yaml','w')
with open('KC2017-A12.20170908-1709.yaml','rb') as config:
	SAMPLES_DICT = yaml.load(config)['SAMPLES']
	sample_dict = {}
	for k in SAMPLES_DICT.keys():
		sample_dict[k] = SAMPLES_DICT[k]['Group']
	yaml.dump(sample_dict, temp_h)
'''
'''
import random
num=random.randint(0,100)
guess=input("guess the number:")
guess=int(guess)
while 0<=guess<=100:
	if guess >num:
		print("guessed too high")
	elif guess <num:
		print("guessed too low")
	else:
		print("you guessed it")
		break
	guess=input("guess again:")
	guess=int(guess)
else:
	print("you quit,the number is :",num)
'''
'''
rawnum=input("please input your number:")
thesum=0
while rawnum!= '.':
	if not rawnum.isdigit():
		print("sorry,please input only number!")
		rawnum=input("input again:")
		continue
	thesum+=int(rawnum)
	rawnum=input("input again:")
print(thesum)
'''
'''
theMax=int(input("give me the upper limint:"))
summ = 0
extra=0
for num in range(1,theMax):
	if num%2 and not num%3:
		summ=summ+num
	else:
print(summ)
print(extra)
'''
'''
num=int(input("please input an number:"))
while num !=1:
	if num%2:
		print(num,end=',')
		num=num*3+1
	else:
		print(num,end=',')
		num=int(num/2)
else:
	print(num)
'''
'''
mystr=input("input a string:")
indxInt=0
result=''
while indxInt < len(mystr)-1:
	if mystr[indxInt] > mystr[indxInt+1]:
		result=result+mystr[indxInt]
	else:
		result=result*2
print(result)
'''
'''
river="Mississippi"
target =input("input a target character to find:")
if river.find(target)==-1:
	print("letter",target,"not found in ",river)
else:
	for index,value in enumerate(river):
		if value == target:
			print("letter found at index :",index)
'''
'''
pokerfile=open("poker-hand-testing.data",'rU')
count=0
paircount=0
for line in pokerfile:
	count+=1
	if line.strip().split(',')[-1]== '1':
		paircount+=1
print("total hands in file :",count)
print("count of pair hands :",paircount)
print("Probability is %5.2f %%"%(100*paircount/float(count)))
'''


#m="ahomebody"
#print(m[int((len(m)-1)/2)+1:])
'''x="acegikmoqsuwy"
y="+bdfhjlnprtvxz"
z=''
for i in range(0,13):
	z=z+x[i]+y[i+1]
print(z)'''
#print("Spam, "*5,"baked beans, ","Spam, "*3,"and Spam.")
'''f=input("input a string:")
for i in range(len(f)-1):
	if f[i]=="o":
		print("the index of 'o' is " ,i)'''
#print([1,2,3,4,45,4,8,4].index(4,0,8))
mylist=[1.6,2.7,3.8,4.9]
newlist=[]
alist=[]
for val in mylist:
	temp=str(val)
	alist.append(temp.split('.'))
for val in alist:
	newlist.append(int(val[0]))
mystr=':'.join(val)
print(mylist)
print(newlist)
print(alist)
print(val)
print(mystr)