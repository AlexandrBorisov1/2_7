import numpy as np
import random as rn
'''a = [[' ']*5 for row in range(5)]

a[1][1] = chr(9689)
a[1][2] = chr(9689)
a[2][1] = chr(9689)
a[2][2] = chr(9689)



b = '\n'.join([''.join(a[i]) for i in range(len(a))])


print(b)'''
#print(f"\033[48;2;{0};{255};{0}m \033[0;0m", end = '')
#print(f"\033[41mJDSDKSJD\033[0m", end = '')
#print(' '.join([chr(i) for i in range(9000,9800)]))
field_arr = np.zeros((21, 12), dtype=int)

blok_L = ([0, 1, 2, 2],[0, 0, 0, 1])
blok_L_inv = ([0, 1, 2, 2],[1, 1, 1, 0])
blok_sq = ([0, 0, 1, 1],[0, 1, 0, 1])
blok_line = ([0, 0, 0, 0],[0, 1, 2, 3])
blok_T = ([0, 1, 2, 1],[0, 0, 0, 1])

a = [i for i in range(21)]*2
b = [0]*21
b.extend([11]*21)
field_walls = (a, b)

y_bottom = [20]*12
x_bottom = [i for i in range(12)]
field_bottom = (y_bottom, x_bottom)

rand_blok = rn.choice([blok_L,blok_L_inv,blok_sq,blok_line,blok_T])

rand_blok = (np.array(rand_blok[0])+1, np.array(rand_blok[1])+5)

field_arr[rand_blok] = 1
field_arr[field_walls] = 2
field_arr[field_bottom] = 2


str_field_arr = '\n'.join([''.join([' ' if field_arr[i, j]==0 else chr(9689) for j in range(field_arr.shape[1])]) for i in range(field_arr.shape[0])])


print(field_arr)
print(str_field_arr)
print(rand_blok)
