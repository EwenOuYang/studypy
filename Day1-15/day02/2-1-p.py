'''
"""
将华氏温度转换为摄氏温度

Version: 0.1
Auth: dezi
'''

f = float(input('华氏温度为'))
c = (f - 32) / 1.8
print('%.1f华氏度= %.1f摄氏度' %(f,c))