'''
判断一个正整数是不是回文素数
Vsersion: 0.1
Author: dezi
Date: 2019-11-10
'''

def is_prime(num):
    for i in range(2,num):
        if num % i ==0:
            return False
    return True if num !=1 else False

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return num == total

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)