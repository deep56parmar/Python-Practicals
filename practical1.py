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
number = 13
count = 0
for i in range(2,number//2):
    if (number % i == 0):
        count+=1
if count == 0:
    print(number , " is prime")
#palindrome

string = "nitin"
string1 = ""
for i in range(len(string)) :
    string1 += string[len(string)-i-1]
if string == string1:
    print ("string is palindrome")

#Fibonacci

number = 5
def fibo(num):
    if num <=1:
         return 1
    else:
        return fibo(num-1) + fibo(num-2)
for i in range(0,number):
    print (fibo(i))
