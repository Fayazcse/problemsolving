#Recursive Function for Power of n
def Power(a,n):
    if n ==0 :
        return 1 
    else:
        return a * Power(a,n-1)
    
#Divisibility by 9
def divisibilityTest(n):
    if n % 9 == 0 and n % 11 == 0 and n % 10!= 0:
        return True
    else:
        return False