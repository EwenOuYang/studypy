'''
设计一个函数返回传入的列表中最大和第二大的元素的值。
Version: 0.1
Author: dezi
Date: 2019-11-12
'''
def get_max2(x):
    m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2
a=[1,3,8,4,9,5,2,7]
if __name__=='__main__':
    print(get_max2(a))



