"""practical 1 """
#print "Hello"
print ("Hello")

#greater in 3 integers
a,b,c = 50,70,30
print(a if (a>b and a>c) else (b if (b>a and b>c) else c))

#Armstring number checker
number = 371
num = number
sum = 0
length = len(str(number))
count = length
while  count:
    x = number % 10
    sum += x ** length
    number = number // 10
    count = count -1
if(sum == num):
    print("number is armstrong")

#prime number


#palindrome
#Fibonacci
