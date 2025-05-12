n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def all_sum() :
    global arr, queries
    for elem in queries :
        new_slice = arr[elem[0]-1:elem[1]:]
        print(sum(new_slice))

all_sum()
