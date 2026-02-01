# Even or odd
def get_even_odd(n):
    return  "Even" if  n % 2 == 0 else "Odd"

n1 = 6
n2 = 7

print(get_even_odd(n1))
print(get_even_odd(n2))

#Multiplication Table

# def multi_table(n,start,end):
#     for i in range(start,end + 1):
#         print(f"{n} x {i} = {n * i}")
        
# start = int(input("Enter the start value like 1 or 2:  "))
# end = int(input("Enter the end value for table: "))
# n = int(input("Enter the number which you want table: "))

# try:
#     multi_table(n,start,end)
# except ValueError:
#     print(f"Value for n must not be zero")
    
    
# Sum of naturals

def sum_naturals(n:int): # using type annotations
    if n < 1:
           raise ValueError("Value must not be negative")
    return n * (n + 1) // 2
    
try:
    print(sum_naturals(10))
    print(sum_naturals(0))
except ValueError:
    print("Value must be positive")
    
# sum of squares og natural numbers

def sumSquares(n):
    return sum(x**2 for x in range(n+1))
    
nos = 10
print(sumSquares(nos))
    
# swapping two variables

def swapTwoVariables(a,b):
    a,b = b,a
    return a,b

swapTwo = lambda a,b : (b,a)

print(swapTwoVariables(3,4))
print(swapTwo(8,9))

# Finding the Closest

def find_closest(n,m):
    closest = 0
    min_difference = float('inf')
    
    
    for i in range(n - abs(m), n + abs(m) + 1):
        if i % m == 0:
            difference = abs(n-i)
            
            if difference < min_difference or  (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest

print(find_closest(13,4))


# Opposite FaceOfDice

def getOppFace(n):
    
    ans = 7 -n
    return ans

print(getOppFace(1))
print(getOppFace(4))

#Nth Term of Ap

def findNthTerm(a1,a2,n):
    nthterm = a1
    d = a2 - a1
    for i in range(1,n):
        nthterm += d
    return nthterm

#using formula

def nthTerm(a1,a2,n):
    return a1 +(n-1) * (a2-a1)



a1 = 5
a2 = 3
n = 19

print(findNthTerm(a1,a2,n))
print(nthTerm(a1,a2,n))


# Reverse Digits

n = 1345
rev = 0

while (n > 0):
    a = n % 10
    print(a)
    rev = rev * 10 + a
    print(rev)
    n = n // 10
    print(n)    
    
    def reverseDigits(n, rev=0):
        if n == 0:
            return rev
        return reverseDigits(n // 10, rev * 10 + n % 10)
    
print(reverseDigits(3456))
       
#Prime testing

def get_prime(n):
    if n <= 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True

print("true") if get_prime(11) else print("false")

print("true") if get_prime(12) else print("false")

#To check if a number is a power of another number


def powNum(x,y):
    if x ==1:
        return y ==1 
    
    pow = 1
    while pow < y:
        pow *= x
        
    return pow == y

print(powNum(5,25))

#using math
import math

def getPower(x,y):
    result = math.log(y) / math.log(x)
    
    return result == math.floor(result)

print(getPower(7,49))

# Distance between two points
import math

x1,x2 = 5,6
y1,y2 = 9,8

dis_res = math.floor(math.sqrt((x2-x1)**2 + (y2-y1)**2))

print(dis_res)