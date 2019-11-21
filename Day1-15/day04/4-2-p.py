"""
输入两个正整数计算它们的最大公约数和最小公倍数

Version: 0.1
Author: dezi
Date: 2019-11-09
"""
a = int(input("请输入数字a："))
b = int(input("请输入数字b："))

if a > b:
    a,b > b,a
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        print("%d 跟 %d的最大公约数是%i"%(a,b,i))
        print("%d 跟 %d的最小公倍数是%i"%(a, b, a*b//i))
        break
