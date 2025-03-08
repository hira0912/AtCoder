def function():
    global N,Q,memo
    N,M = map(int,input().split())
    Q = []
    memo = []

    for _ in range(M):
        u,v,w = map(int,input().split())
        Q.append((u-1,v-1,w))

    result = dfs(0,0)

    print(result)
    return

def dfs(pre,total):
    if(pre==N-1):
        return total

    result = 2**60
    
    for u,v,w in Q:
        if u == pre and v not in memo:
            memo.append(v)
            result = min(result,dfs(v,total^w))
            memo.remove(v)
        elif v == pre and u not in memo:  
            memo.append(u)
            result = min(result,dfs(u,total^w))
            memo.remove(u)
    return result

if __name__ == "__main__":
    function()