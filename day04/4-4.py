"""
九九乘法表

Version: 0.1
Author: dezi
"""
i=0
while i<9:
    i+=1
    for j in range(1,10):
        print("%d X %d = %d" %(i,j,i*j))
