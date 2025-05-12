A = input()

# Please write your code here.

def same(string) :
    A = string[0]
    for i in range (len(string)) :
        if string[i] == A :
            continue
        else :
            return False
    return True

        
if same(A) :
    print("No")
else :
    print("Yes")