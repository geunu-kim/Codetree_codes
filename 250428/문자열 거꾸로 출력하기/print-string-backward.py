while True :
    a = input()
    if a == 'END' :
        break
    else :
        b = list(a)
        b.reverse()
        for elem in b :
            print(elem,end="")
        print()