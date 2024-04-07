def function():
    # initialize
    H,W = map(int,input().split())
    MAP = []
    Start = []
    for _ in range(H):
        MAP.append(str(input()))
    
    # Start and Goal initialize
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if(MAP[i][j]=='S'):
                Start.append([i,j,0])
                MAP[i] = MAP[i].replace('S','.')
            if(MAP[i][j]=='T'):
                Goal = [i,j,0]
                MAP[i] = MAP[i].replace('T','.')
    
    # MAP test_print
    for c in MAP:
        print(c)


if __name__ == "__main__":
    function()