import math
radius = float(input('请输入圆的半径：'))

circumference = radius * math.pi *2
area=(radius**2)*math.pi

print('圆的周长为%.2f'%(circumference))
print('圆的面积为%.2f'%(area))

circum=str(circumference)
area=str(area)
print('圆的周长为'+circum)
print('圆的面积为'+area)
