A = input().split()
Aa = str(A[0])
Ab = int(A[1])

B = input().split()
Ba = str(B[0])
Bb = int(B[1])

C = input().split()
Ca = str(C[0])
Cb = int(C[1])



if Aa == "Y" and Ab >= 37 :
    Aa = "A"
elif Aa == "Y" and Ab < 37 :
    Aa = "C"
elif Aa == "N" and Ab >= 37 :
    Aa = "B"
else :
    Aa = "D"

if Ba == "Y" and Bb >= 37 :
    Ba = "A"
elif Ba == "Y" and Bb < 37 :
    Ba = "C"
elif Ba == "N" and Bb >= 37 :
    Ba = "B"
else :
    Ba = "D"

if Ca == "Y" and Cb >= 37 :
    Ca = "A"
elif Ca == "Y" and Cb < 37 :
    Ca = "C"
elif Ca == "N" and Cb >= 37 :
    Ca = "B"
else :
    Ca = "D"



if Aa and Ba and Ca != "A" :
    print("N")
elif (Aa == "A" and Ba != "A" and Ca != "A") or (Ba == "A" and Aa != "A" and Ca != "A") or (Ca == "A" and Ba != "A" and Aa != "A") :
    print("N")
else :
    print("E")