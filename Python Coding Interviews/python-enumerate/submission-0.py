from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    index = -1
    for i, num in enumerate(nums):
        if num == 7:
            index = i

            break

    return index


def get_dist_between_sevens(nums: List[int]) -> int:
    idx_first_sev = get_index_of_seven(nums)
    idx_sec_sev = 0
    
    for index, num in enumerate(nums):
        if index == idx_first_sev:
            continue
        elif num == 7:
            idx_sec_sev = index

            break

    return idx_sec_sev - idx_first_sev



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
