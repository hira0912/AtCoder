def function():
    N = int(input())
    N_str = str(N)

    ans = 'Yes'
    for i in range(1,len(N_str)):
        if(N_str[i]>=N_str[i-1]):
            ans = 'No'
            break
    print(ans)

if __name__ == "__main__":
    function()