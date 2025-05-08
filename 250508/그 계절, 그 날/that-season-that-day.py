Y, M, D = map(int, input().split())

# Please write your code here.
def weather(x,y,z) :
    if x % 4 == 0 and x % 100 == 0 :
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12 :
            if z >= 1 and z <= 31 :
                if y == 12 or y == 1 :
                    return "Winter"
                elif y == 3 or y == 5 :
                    return "Spring"
                elif y ==7 or y == 8 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"
        elif y == 2 :
            if z >= 1 and z <= 28 :
                return "Winter"
            else :
                return "-1"
        elif y == 4 or y == 6 or y == 9 or y == 11 :
            if z >= 1 and z <= 30 :
                if y == 4 :
                    return "Spring"
                elif y == 6 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"
    elif x % 4 == 0 or (x % 4 == 0 and x % 100 == 0 and x % 400 == 0) :
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12 :
            if z >= 1 and z <= 31 :
                if y == 12 or y == 1 :
                    return "Winter"
                elif y == 3 or y == 5 :
                    return "Spring"
                elif y ==7 or y == 8 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"
        elif y == 2 :
            if z >= 1 and z <= 29 :
                return "Winter"
            else :
                return "-1"
        elif y == 4 or y == 6 or y == 9 or y == 11 :
            if z >= 1 and z <= 30 :
                if y == 4 :
                    return "Spring"
                elif y == 6 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"
    else :
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12 :
            if z >= 1 and z <= 31 :
                if y == 12 or y == 1 :
                    return "Winter"
                elif y == 3 or y == 5 :
                    return "Spring"
                elif y ==7 or y == 8 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"
        elif y == 2 :
            if z >= 1 and z <= 28 :
                return "Winter"
            else :
                return "-1"
        elif y == 4 or y == 6 or y == 9 or y == 11 :
            if z >= 1 and z <= 30 :
                if y == 4 :
                    return "Spring"
                elif y == 6 :
                    return "Summer"
                else :
                    return "Fall"
            else :
                return "-1"


print(weather(Y,M,D))