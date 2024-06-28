
A = [8,7,6,5,4,3,2,1]

A = sorted(A)

for i in range(len(A)//2):
    # print(i)
    # print("")
    print(A[i], A[~i])

 
# --> [~i] ifadesi bitwise NOT operatörüdür yani ters indexleme yapa
# -> bu da demek oluyor ki i = 0 iken ~i = -1 
# > i = 1 iken ~i = -2










