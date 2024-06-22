def function():
    N = int(input())
    ans = 0
    for _ in range(N):
        if(str(input())=='Takahashi'):
           ans += 1
    print(ans)
    return

if __name__ == "__main__":
    function()