""" Write a python program to implement insertion sort and merge sort using lists """

import random

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
        
    return my_list

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr [j]
            j -= 1
        arr[j+1] = key
        
my_list = []
for i in range(10):
    my_list.append(random.randint(0,999))
    
print('\n Unsorted list')
print(my_list)
print('sorting using insertion sort')
insertion_sort(my_list)
print(my_list)

my_list = []
for i in range(10):
    my_list.append(random.randint(0,999))

print('\n Unsorted list')
print(my_list)
print('Sorting using merge sort')
merge_sort(my_list)
print(my_list)