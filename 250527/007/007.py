secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class secret :
    def __init__ (self,secret_code,meeting_point,time) :
        self.s = secret_code
        self.m = meeting_point
        self.t = time

secret1 = secret(secret_code,meeting_point,time)

print("secret code :",secret1.s)
print("meeting point :",secret1.m)
print("time :",secret1.t)


