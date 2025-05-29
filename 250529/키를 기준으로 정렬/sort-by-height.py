n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class People :
    def __init__ (self, name, height, weight) :
        self.name = name
        self.height = height
        self.weight = weight

people = [People(name[i], height[i], weight[i]) for i in range (n)]
people.sort(key = lambda x : x.height)

for People in people :
    print(People.name, People.height, People.weight)


