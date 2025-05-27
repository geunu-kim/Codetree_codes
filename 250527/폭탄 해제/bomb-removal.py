unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb :
    def __init__ (self,a,b,c) :
        self.code = a
        self.color = b
        self.seconds = c

Bomb2 = Bomb(unlock_code, wire_color, seconds)

print("code :",Bomb2.code)
print("color :",Bomb2.color)
print("second :",Bomb2.seconds)