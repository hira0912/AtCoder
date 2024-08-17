def function():
    A,B,C = map(int,input().split())
    if(B<C):
        if(B<A and A<C):
            print('No')
        else:
            print('Yes')
    else:
        if(B<A and A<C+24):
            print('No')
        elif(B<A+24 and A<C):
            print('No')
        else:
            print('Yes')
    return

if __name__ == "__main__":
    function()