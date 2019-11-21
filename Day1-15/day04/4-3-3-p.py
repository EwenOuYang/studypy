'''
    *
   ***
  *****
 *******
*********
Version: 0.1
Author: dezi
Date: 2019-11-09
'''
for i in range(5):
    for j in range(5-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()