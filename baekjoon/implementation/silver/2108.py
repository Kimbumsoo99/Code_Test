import sys
input = sys.stdin.readline

N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

# round는 사사오입의 원칙으로 짝수의 가깝게 반올림함 3.5 -> 4, 4.5 -> 4

print(int(sum(nums) / len(nums) + (0.5 if sum(nums) >= 0 else -0.5)))
sort_nums = sorted(nums)
print(sort_nums[int(len(nums)/2)])


more_nums = {}
for i in sort_nums:
    if not (i in more_nums.keys()):
        more_nums[i] = 1
    else:
        more_nums[i] += 1

mode_num = []
for i in set(sort_nums):
    if max(more_nums.values()) == more_nums[i]:
        mode_num.append(i)
print(sorted(mode_num)[1] if len(mode_num) > 1 else sorted(mode_num)[0])

print(sort_nums[-1] - sort_nums[0])