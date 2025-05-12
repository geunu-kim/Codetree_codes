A = input()

# Please write your code here.

def palindrome (text) :
    reverse_text = text[::-1]
    if reverse_text == text :
        return True
    else :
        return False

if palindrome(A) :
    print("Yes")
else :
    print("No")
