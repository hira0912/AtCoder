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
                Start.append([i,j,6]) # energy 6 on start
                MAP[i] = MAP[i].replace('S','.')
            if(MAP[i][j]=='T'):
                Goal = [i,j]
                MAP[i] = MAP[i].replace('T','.')

    # move node
    def move():
        new_Start = []
        new_Goal = []
        new_Start.append(Start[0])

        def check_Goal(pos):
            if(pos[0]==Goal[0] and pos[1] == Goal[1]):
                new_Goal.append([pos[0],pos[1]])

        def check_nextStart(pos):
            if(pos[2] > 1 and MAP[pos[0]][pos[1]] != '#'):
                next_Start.append([pos[0],pos[1],pos[2]-1])
                
        while(new_Start):
            next_Start = []
            for c in new_Start:
                if(c[0] != 0):
                    pos = [c[0]-1,c[1],c[2]]
                    check_Goal(pos)
                    check_nextStart(pos)
                if(c[0] != H-1):
                    pos = [c[0]+1,c[1],c[2]]
                    check_Goal(pos)
                    check_nextStart(pos)
                if(c[1] != 0):
                    pos = [c[0],c[1]-1,c[2]]
                    check_Goal(pos)
                    check_nextStart(pos)
                if(c[1] != W-1):
                    pos = [c[0],c[1]+1,c[2]]
                    check_Goal(pos)
                    check_nextStart(pos)
            if(new_Goal):break
            new_Start = next_Start

        return new_Goal

    new_Goal = move()

    # check Goal and print
    if(new_Goal):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    function()