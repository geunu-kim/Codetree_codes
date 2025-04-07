n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
b = min(a)
cnt = a.count(b)

print(b, cnt)