#take 10 inputs and print avg 
n=input("enter any numbers:")
num=n.split()
print("\n")
print("enter all numbers",num)
sum=0
for i in num:
	sum+=int(i)
print("sum of numbers",sum)
avg=sum/len(num)
print(avg)

str1= input('Enter the string:')
freq = {} 
for i in str1: 
     if i in freq: 
        freq[i] += 1
     else: 
        freq[i] = 1
print ("Count of all characters in string is :\n",str(freq))

#n  fibonacci series
n=int(input("enter the limit"))
a=0
b=1
count=0
if n<0:
	print("enter the positive number")
elif n==1:
	print("fibonacci series upto ",n)
	print(a)
else:
	print("fibonacci series are:")
	while count<n:
		print(a)
		sum=a+b
		a=b
		b=sum
		count=count+1
	
#no. of characters in string
	a = "refrigerator"
count=0
for i in a:
	count=count+1
print(count)

#pattern 
def star(n):
	for i in range (0,n):
		for j in range(0,i+1):
			print("*",end=" ")
		print("\r")
n=4
star(n)

#count occurance of substring
s="ram is a good boy"
print(s.count("ram"))

#to upper and lower case
txt = "HelloWorld" [::-1]
print(txt.upper())
print(txt.lower())