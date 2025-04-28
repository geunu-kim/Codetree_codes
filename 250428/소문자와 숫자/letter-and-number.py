a = input()

for i in range (len(a)) :
    if a[i].isalpha() == True :
        print(a[i].lower(), end="")
    elif a[i].isdigit() == True :
        print(a[i], end="")
    else :
        continue



