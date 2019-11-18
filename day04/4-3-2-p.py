'''
    *
   **
  ***
 ****
*****
Version: 0.1
Author: dezi
Date: 2019-11-09
'''

for i in range(5):
    for j in range(5):
        if j < 5-i-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

