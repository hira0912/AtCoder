import itertools
def function():
    A = list(map(int,input().split()))
    data = list(map(int,input().split()))
    A += data
    data = list(map(int,input().split()))
    A += data

    B_list = [0,1,2,3,4,5,6,7,8]
    B = list(itertools.combinations(tmp,5))
    for c in reversed(B):
        if((0 in c and 1 in c and 2 in c) or (3 in c and 4 in c and 5 in c) or (6 in c and 7 in c and 8 in c) or (0 in c and 3 in c and 6 in c) or (1 in c and 4 in c and 7 in c) or (2 in c and 5 in c and 8 in c) or (0 in c and 4 in c and 8 in c) or (2 in c and 4 in c and 6 in c)): 
                B.remove(c)

    print(B)



if __name__ == "__main__":
    function()