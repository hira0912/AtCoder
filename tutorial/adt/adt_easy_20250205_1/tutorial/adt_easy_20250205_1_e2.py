import itertools

def function():
    KT = []
    K = [0,1,2,3,4,5,6,7,8,9]
    for i in range(10):
        if(i==0):
            for j in range(1,len(K)):
                KT.append(K[j])
        else:
            p_list = list(itertools.combinations(K,i+1))
            for c in p_list:
                k = ''
                for j in range(len(c)):
                    k += str(c[len(c)-j-1])
                KT.append(int(k))
    KT.sort()

    N = int(input())
    print(KT[N-1])
    return

if __name__ == "__main__":
    function()