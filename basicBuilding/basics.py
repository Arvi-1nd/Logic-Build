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