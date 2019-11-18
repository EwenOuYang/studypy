'''
$$x_1 + x_2 + x_3 + x_4 = 8$$
事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案。想到这一点问题的答案就呼之欲出了。

$$C_M^N =\frac{M!}{N!(M-N)!}, \text{(M=7, N=3)} $$
Version: 0.1
Author: dezi
Date: 2019-11-10
'''
def factorial(num):
    '''求阶乘'''
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))

fm = factorial(m)
fn = factorial(n)
fmn = factorial(m-n)

print(fm//fn//fmn)