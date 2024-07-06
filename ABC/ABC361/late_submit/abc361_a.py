def function():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.insert(K,X)
    print(*A)
    return

if __name__ == "__main__":
    function()