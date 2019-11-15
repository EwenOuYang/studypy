'''
打印杨辉三角
Version: 0.1
Author: Dezi
Date: 2019-11-14
'''
def pascal_triangle():
    num = int(input('请出入杨辉三角的行数：'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col]=1
            else:
                yh[row][col]=yh[row-1][col]+yh[row-1][col-1]
            print(yh[row][col],end='\t')
        print()

if __name__ == '__main__':
     pascal_triangle()






