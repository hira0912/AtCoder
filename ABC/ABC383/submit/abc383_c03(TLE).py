from collections import deque

def function():
    H, W, D = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(input().strip()))
    
    H1 = []
    H2 = []
    for i in range(H):
        for j in range(W):
            if A[i][j] == 'H':
                H1.append(i)
                H2.append(j)

    queue = deque()
    
    for i in range(len(H1)):
        queue.append((H1[i], H2[i], D)) 
    
    while queue:
        B1, B2, remaining_D = queue.popleft()
        
        if remaining_D == 0:
            continue
        
        vector = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for c in vector:
            new_B1, new_B2 = B1 + c[0], B2 + c[1]
            
            if new_B1 < 0 or new_B1 >= H or new_B2 < 0 or new_B2 >= W:
                continue
            
            if A[new_B1][new_B2] == '#':
                continue
            
            if A[new_B1][new_B2] == '.':
                A[new_B1][new_B2] = '@'

            queue.append((new_B1, new_B2, remaining_D - 1))
    
    total = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == '@' or A[i][j] == 'H':
                total += 1
    print(total)
    return

if __name__ == "__main__":
    function()