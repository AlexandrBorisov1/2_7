#Разработайте функцию holes_count(number), которая подсчитывает количество отверстий в заданном числе number.
# Например, в цифре 8 два отверстия, в цифре 9 - одно. В числе 146 - два отверстия.

def holes_count(number):
    holes_dict = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
    str_num = str(number)
    col_holes = 0
    for i in str_num:
        col_holes += holes_dict[i]
    return col_holes

