n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Info :
    def __init__ (self,a,b,c) :
        self.n = a
        self.a = b
        self.c = c

sorted_name = sorted(name)
sorted_name_2 = sorted_name[-1]
where_sorted_name_2 = name.index(sorted_name_2)

Info2 = Info(sorted_name_2,street_address[where_sorted_name_2],region[where_sorted_name_2])

print("name",Info2.n)
print("addr",Info2.a)
print("city",Info2.c)