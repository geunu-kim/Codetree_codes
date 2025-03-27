N = int(input())
arr = list(map(float,input().split()))
total_arr = sum(arr)
average = total_arr / N

if average >= 4.0 :
    print(f"{average:.1f}")
    print("Perfect")
elif average >= 3.0 :
    print(f"{average:.1f}")
    print("Good")
else :
    print(f"{average:.1f}")
    print("Poor")

