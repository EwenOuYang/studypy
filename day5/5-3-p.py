'''
输出1-100内的素数
说明：素数指的是只能被1和自身整除的正整数（不包括1）。

Version: 0.1
Author: dezi
Date: 2019-11-9
'''
import math


for i in range(1,100):
    end = int(math.sqrt(i))+1;
    is_prime=True
    for j in range(end,1,-1):
        if i % j ==0:
            is_prime=False
    if is_prime:
        print(i)


