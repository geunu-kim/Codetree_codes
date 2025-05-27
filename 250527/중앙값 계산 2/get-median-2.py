n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
n2 = n // 2 ; arr2 = []

for i in range (n2 + 1) :
    arr2 = arr[:(2*i + 1):]
    sorted_arr2 = sorted(arr2)
    middle_value = sorted_arr2[len(sorted_arr2)//2]
    print(middle_value, end=" ")