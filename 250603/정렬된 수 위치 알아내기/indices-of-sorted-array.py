n = int(input())
sequence = list(map(int, input().split()))
sequence_3 = sequence[:]
# Please write your code here.
sequence.sort()

sequence_2 = [] ; num = 1

for elem in sequence :
    sequence_2.append((num, elem))
    num += 1

for elem in sequence_3 :
    for i, item in enumerate(sequence_2) :
        if elem == item[1] :
            print(item[0], end=" ")
            del sequence_2[i]
            break
        else :
            continue