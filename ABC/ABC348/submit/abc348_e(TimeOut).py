from collections import deque

def function():
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    for n in range(N):
        q = deque()
        q.append(n)
        upper = [-1] * N
        upper[n] = -2

        def BFS():
            while q:
                now = q.popleft()
                for nxt in g[now]:
                    if upper[nxt] == -1:
                        upper[nxt] = now
                        q.append(nxt)

        BFS()

        ans = []




if __name__ == "__main__":
    function()