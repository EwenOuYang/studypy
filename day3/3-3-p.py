"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: dezi
"""
a = int(input('请输入长度a：'))
b = int(input('请输入长度b：'))
c = int(input('请输入长度c：'))
if (a+b > c) and (a+c >b) and (b+c >a):
    perimeter = a + b + c
    p=(a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c)) **0.5
    print('三角形的周长为%d'%(perimeter))
    print('三角形的面积为%d'%(area))
else:
    print('输入的长度有误')