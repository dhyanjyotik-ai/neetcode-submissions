from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    newarr = []
    for sublist in nested_arr:
        maxi = sublist[0]
        for element in sublist[1:]:
            if element > maxi:
                maxi = element
        newarr.append(maxi)
    return newarr


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
