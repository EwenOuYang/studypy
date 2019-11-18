'''
实现最大公约数以及最小公倍数的函数
Version: 0.1
Author: dezi
Date: 2011-11-10
'''
#最大公约数
def gcd(m,n):
    if m > n:
        m,n = n,m
    for i in range(m,0,-1):
        if m % i ==0 and n % i==0:
            return i

#最小公倍数
def lcm(m,n):
    return m*n//gcd(m,n)

print(gcd(48,94))
print(lcm(48,94))