list=[1,3,4,5,6,7,8]
def rotate_list_right(lst):
    if len(lst)<=1:
        return lst.copy()
    return [list[-1]]+ lst[:-1]
print("rotated list:", rotate_list_right(list))

