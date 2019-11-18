'''
判断一个数是不是回文数，例如n=124421
'''

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return num == total
print(is_palindrome(123321))

