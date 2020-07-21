# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    if len(arrA) == 0:
        return list_right
    elif len(arrB) == 0:
        return list_left
    
    x = 0
    y = 0
    merged_idx = 0
    while merged_idx < elements:
        if arrA[x] <= arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
        else:
            merged_arr.append(arrB[y])
            y += 1
            
        # If we are at the end of one of the lists we can take a shortcut
        if y == len(arrB):
            # Reached the end of right
            # Append the remainder of left and break
            merged_arr += arrA[x:]
            break
        elif x == len(arrA):
            # Reached the end of left
            # Append the remainder of right and break
            merged_arr += arrB[y:]
            break




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # if len(arr) > 1:
    #     return arr
    # else:
    #     middle = len(arr)//2
    #     left = arr[:middle]
    #     right = arr[middle:]

    #     return merge(mere_sort(left), merge_sort(right))


    # return arr

    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        # arr = merge(left, right)

        x = 0
        y = 0
        merged_idx = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[merged_idx] = left[x]
                x += 1

            else:
                arr[merged_idx] = right[y]
                y += 1
            merged_idx += 1

        while x < len(left):
            arr[merged_idx] = left[x]
            x += 1
            merged_idx += 1

        while y < len(right):
            arr[merged_idx] = right[y]
            y += 1
            merged_idx += 1


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     if len(arr) > 1:
#         middle = len(arr)//2
#         left = arr[:middle]
#         right = arr[middle:]

#         merge_sort(left)
#         merge_sort(right)

#         # arr = merge(left, right)

#         x = 0
#         y = 0
#         merged_idx = 0

#         while x < len(left) and y < len(right):
#             if left[x] < right[y]:
#                 arr[merged_idx] = left[x]
#                 x += 1

#             else:
#                 arr[merged_idx] = right[y]
#                 y += 1
#             merged_idx += 1

#         while x < len(left):
#             arr[merged_idx] = left[x]
#             x += 1
#             merged_idx += 1

#         while y < len(right):
#             arr[merged_idx] = right[y]
#             y += 1
#             merged_idx += 1


#     return arr

