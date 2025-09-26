#Coverting fahrenheit to Celsius
def covertingTemps(fahrenheit: float) -> float:
#return float value, temp into celsius
    return (fahrenheit-32) *5.0/9.0



#Computing the Fibonacci number with iteration
def fibonacciNumber(n: int) -> int:
    #n = 0 returns 0, n= 1 returns 1, for n > 1 return the the sum of the previous 2
    if n < 0:
        return None
    #return 0
    elif n == 0:
        return 0
    #return 1
    elif n == 1:
        return 1
    #return the sum of the previous 2
    else:
        r, c = 0, 1

        for _ in range(2, n + 1):
            r, c = c, r + c
        return c 
        

 #Printing out the functions       
print("32F Celsius:", covertingTemps(32))
print("Fibonacci(8):", fibonacciNumber(8))
    

