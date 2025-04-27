input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for elem in queries :
    if elem == 1 :
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    elif elem == 2 :
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)
    elif elem == 3 :
        input_str_2 = list(input_str)
        input_str_2.reverse()
        input_str = ''.join(input_str_2)
        print(input_str)