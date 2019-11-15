'''
计算年月日是今年的第几天
Version：0.1
Author：dezi
Date：2019-11-12
'''
def is_year(year=2000):
    if (year % 4==0 and year %100!=0) or year % 400 ==0:
        return 29
    else:
        return 28
def is_day(year=2000,month=1,days=31):
    day = 0
    for i in range(1,month):
        if i in (1,3,5,7,8,10,12):
            day +=31
        elif i in (4,6,9,11):
            day +=30
        else:
           day+=is_year(year)
    return day+days
if __name__ == '__main__':
    print(is_day(2019,11,12))





