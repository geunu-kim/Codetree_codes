a = input()
tot = 0

for i in range (len(a)) :
    if a[i].isdigit() == True :
        tot += int(a[i])

print(tot)