'''
正数的反转
例如 12345变为54321
Version: 0.1
Author: dezi
'''

num=int(input("请输入一个数字："))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(reverse_num)