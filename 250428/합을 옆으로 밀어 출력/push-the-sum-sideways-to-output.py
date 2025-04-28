n = input()
tot = 0

for i in range (int(n)) :
    a = input()
    tot += int(a)


tot = str(tot)

print(tot[1:] + tot[0])