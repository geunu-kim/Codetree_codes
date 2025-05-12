text = input()
pattern = input()

# Please write your code here.
def inside(x,y) :
    if y in x :
        index = x.find(y)
        return index
    else :
        return -1

print(inside(text,pattern))