year=int(input('请输入年份：'))

if (year%4==0 and year%100!=0) or year % 400 ==0:
    year=str(year)
    print(year+'是闰年')
else:
    year = str(year)
    print(year + '不是闰年')
