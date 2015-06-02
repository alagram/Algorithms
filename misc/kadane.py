# finds contiguous maximum subarray in one-dimensional array in linear time

def find_max_subarray(a_list):
    max_till_here = [0] * len(a_list)
    max_value = 0

    for i in range(len(a_list)):
        max_till_here[i] = max(a_list[i], max_till_here[i-1]+ a_list[i])
        max_value = max(max_value, max_till_here[i])
    return max_value



print find_max_subarray([1, 4, -1, 3, -5, 4]) # 7
