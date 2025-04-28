a = input()

for i in range (len(a)) :
    if 'A' <= a[i] and a[i] <= 'Z' :
        print(a[i].lower(), end="")
    else :
        print(a[i].upper(), end="")



