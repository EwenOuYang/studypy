"""
输入一个正整数判断是不是素数

Version: 0.1
Author: dezi
"""
from math import sqrt
number=int(input("输入一个正整数："))
end = int(sqrt(number))
is_lead=True
for i in range(2,end+1):
    if number % i ==0:
        is_lead=False
        break
if is_lead and number != 1:
    print('%d是素数'%(number))
else:
    print('%d是合数'%(number))