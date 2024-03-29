'''
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
Version: 1.0
Author: dezi
Date: 2019-11-16
'''
from math import sqrt
class PtoP(object):

    def __init__(self,x,y):
        """
        初始化方法
        :param x:
        :param y:
        """
        self.x=x
        self.y=y

    def moveto(self,x,y):
        """
        移动到指定点
        :param x:
        :param y:
        :return:
        """
        self.x=x
        self.y=y

    def moveby(self,dx,dy):
        """
        移动指定的增量
        :param dx:
        :param dy:
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        """
        计算与另一个点的距离
        :param other:
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2+dy**2)

    def __str__(self):
        return '(%s,%s)'%(str(self.x),str(self.y))

def main():
    p1 = PtoP(3,5)
    p2 = PtoP(2,1)
    print(p1)
    print(p2)
    p2.moveby(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()