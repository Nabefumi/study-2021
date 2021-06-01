'''
Write recursive function which calculates a**b (a to the power of b) 
recursively without using the power operation

'''
#Problem3

def pow_k(x, n):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x
    
print(pow_k(2, 20))