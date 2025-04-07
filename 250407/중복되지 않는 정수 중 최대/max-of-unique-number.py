n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums_2 = [] ; b = 0

for elem in nums :
    a = nums.count(elem)
    if a >= 2 :
        pass
    else :
        b = elem
        nums_2.append(b)


if len(nums_2) >= 1 :
    print(max(nums_2))
else :
    print(-1)



