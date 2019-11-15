"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: dezi
"""

value = float(input('请输入长度：'))
unit = str(input('请输入单位：'))
if unit=='英寸' or unit=='in':
    print('%.1f英寸等于%.1f里米'%(value,value*2.54))
elif unit=='厘米' or unit=='cm':
    print('%1f厘米等于%.1f英寸'%(value,value/2.54))
else:
    print('输入的单位有误')
