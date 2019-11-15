'''
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
Version: 0.1
Author: dezi
'''

for x in range(0,20):
    for y in range(0,33):
        z = 100 -x -y
        if 5*x + 3*y + z/3 == 100:
            print("%d 只公鸡 + %d 只母鸡 + %d 只小鸡" %(x,y,z))
