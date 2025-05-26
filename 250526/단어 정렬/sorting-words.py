n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
sorted_word = sorted(word)

for elem in sorted_word :
    print(elem)