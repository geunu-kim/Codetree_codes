n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
sorted_nums = sorted(nums)
sorted_nums.sort(reverse=True)

cnt = 0

for i in range (n) :
    if (sorted_nums[i] + sorted_nums[2*n - 1 - i]) >= cnt :
        cnt = (sorted_nums[i] + sorted_nums[2*n - 1 - i])

print(cnt)