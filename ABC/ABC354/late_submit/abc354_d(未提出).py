def function():
    A,B,C,D = map(int,input().split())
    A += 10**9
    B += 10**9
    C += 10**9
    D += 10**9
    data = [[2,1,0,1],[1,2,1,0],[2,1,0,1],[1,2,1,0]]
    num = 0

    A_mod = A%4
    B_mod = B%4
    C_mod = C%4
    D_mod = D%4

    if(A_mod==0):
        A_rel = A
    else:
        A_rel = A+4-A_mod
    if(B_mod==0):
        B_rel = B
    else:
        B_rel = B+4-B_mod
    C_rel = C-C_mod
    D_rel = D-D_mod

    num += (C_rel-A_rel) * (D_rel-B_rel) * 16



    print(num*2)

if __name__ == "__main__":
    function()