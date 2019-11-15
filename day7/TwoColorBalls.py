'''
双色球
Version：0.1
Author: dezi
Date: 2019-11-14
'''
from random import randint,randrange,sample
def random_ball():
    '''
    随机选择一组号码
    :return:
    '''
    red_balls = [x for x in range(1,34)]
    select_ball=[]
    select_ball= sample(red_balls,6)
    select_ball.sort()
    select_ball.append(randint(1,16))
    return select_ball

def display(balls):
    '''
    输出列表中的双色球号码
    :param balls:
    :return:
    '''
    for index,ball in enumerate(balls):
        if index == len(balls)-1:
            print('|',end=' ')
        print('%02d' % ball, end=' ')
    print()

def main():
    n = int(input('随机选几注：'))
    for _ in range(n):
        display(random_ball())

if __name__ == '__main__':
    main()


