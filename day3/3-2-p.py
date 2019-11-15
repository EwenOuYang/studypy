"""
百分制成绩转换为等级制成绩。
Version: 0.1
Author: dezi
"""
score=int(input('请输入你的成绩'))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("E")