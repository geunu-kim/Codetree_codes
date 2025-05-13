n = int(input())

# Please write your code here.
def logic (x) :
    if x == 0 :
        return
    
    logic (x-1)
    print("HelloWorld")

logic(n)

