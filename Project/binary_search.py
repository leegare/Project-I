def binary_search(sorted_list, goal):
    length = len(sorted_list)
    left = 0
    right = length - 1

    while left <= right:
        if goal < sorted_list[right] and goal > sorted_list[left]:
            piv = int((right+left)/2)            # Pivot
            if goal == sorted_list[piv]:
                return piv
            elif goal > sorted_list[piv]:
                left = piv
            else:
                right = piv
        # Edge Cases
        elif goal == sorted_list[right] or goal == sorted_list[left]:
            if goal == sorted_list[right]:
                return right
            else:
                return left
        else:
            break
    return -1
