def solution(nums):
    answer = 0
    N = len(nums) // 2
    num_set = set(nums)
    num_set_len = len(num_set)
    if N > num_set_len:
        answer = num_set_len
    else:
        answer = N
    return answer