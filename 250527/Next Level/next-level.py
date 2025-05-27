user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Next :
    def __init__ (self,a = "codetree",b="10") :
        self.id = a
        self.lv = b


Next1 = Next()
print("user",Next1.id,"lv",Next1.lv)

Next2 = Next(user2_id,user2_level)
print("user",Next2.id,"lv",Next2.lv)



