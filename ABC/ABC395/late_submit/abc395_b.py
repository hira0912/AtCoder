def function():
    N = int(input())

    for i in range(N):
        str = ''
        leng = min(i,abs(N-i-1))
        for j in range(leng):
            if(j%2==0):
                str+= '#'
            else:
                str+= '.'        

        for j in range(leng,N-leng):
            if(leng%2==0):
                str+= '#'
            else:
                str+= '.'  

        for j in range(N-leng,N):
            if(j%2!=N%2):
                str+= '#'
            else:
                str+= '.'        

        print(str)
    return

if __name__ == "__main__":
    function()