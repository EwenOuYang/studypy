'''
生成斐波那契数列的前20个数。
斐波那契函数 1 1 2 3 5 8 13 21 34 55 89...
Version: 0.1
Author: dezi
date: 2019-11-9
'''

a = 0
b = 1
for i in range(20):
    a,b = b,a+b
    print(a,end=' ')


