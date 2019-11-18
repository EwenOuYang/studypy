'''
判断一个数是不是素数
Version: 0.1
Author: dezi
Date: 2011-11-10
'''
def is_prime(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True if num>1 else False

print(is_prime(11))