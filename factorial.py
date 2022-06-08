# to compute factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
    
# nCr formula
def ncr(n, r):
    return (factorial(n)//((factorial(r)*factorial((n-r)))))

# Function to demonstrate printing pattern triangle
def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n+1):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k+1):
            print(end="   ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing number
            #print(ncr(i,j), end=" ")
            print("%3d" % (ncr(i,j)), end="   ")
        
        #print("*", end="")
     
        # ending line after each row
        print("\r")

print("This program is to genrate a Pascal Triangle with n rows.")
print("---------------------------------------------------------")
print()
triangle(12)
