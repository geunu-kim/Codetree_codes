a, b = map(int, input().split())

# Please write your code here.
def condition(n) :
    tot = 0
    n_list = list(str(n))
    for j in range (len(n_list)) :
        if int(n_list[j]) in [3, 6, 9] :
            tot += int(n_list[j])
            return True
        else :
            tot += int(n_list[j])
    if tot % 3 == 0 :
        return True

cnt = 0 

for i in range (a,b+1,1) :
    if condition(i) == True :
        cnt += 1

print(cnt)
