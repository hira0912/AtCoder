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
                Goal = [i,j]
                MAP[i] = MAP[i].replace('T','.')

    # Med initialze
    N = int(input())
    Med = []
    for _ in range(N):
        Med_split = list(map(int,input().split()))
        Med.append([Med_split[0]-1,Med_split[1]-1,Med_split[2]])

   # move node
    def move():
        new_Start = []
        new_Goal = []
        new_Med = set()
        new_Start=Start

        def check_Goal(pos):
            if(pos[0]==Goal[0] and pos[1] == Goal[1]):
                new_Goal.append([pos[0],pos[1]])

        def check_Med(pos):
            for i in range(len(Med)):
                if(pos[0]==Med[i][0] and pos[1]==Med[i][1]):
                    new_Med.add(i)

        def check_nextStart(pos):
            if(pos[2] > 1 and MAP[pos[0]][pos[1]] != '#'):
                next_Start.append([pos[0],pos[1],pos[2]-1])
        
        def check(pos):
            check_Goal(pos)
            check_Med(pos)
            check_nextStart(pos)
                
        while(new_Start):
            next_Start = []
            for c in new_Start:
                if(c[2] == 0):
                    pos = [c[0],c[1],c[2]]
                    check_Med(pos)
                    break
                if(c[0] != 0):
                    pos = [c[0]-1,c[1],c[2]]
                    check(pos)
                if(c[0] != H-1):
                    pos = [c[0]+1,c[1],c[2]]
                    check(pos)
                if(c[1] != 0):
                    pos = [c[0],c[1]-1,c[2]]
                    check(pos)
                if(c[1] != W-1):
                    pos = [c[0],c[1]+1,c[2]]
                    check(pos)
            if(new_Goal):break
            new_Start = next_Start

        return new_Goal,new_Med

    while(Start):
        new_Goal,new_Med = move()

        # check Goal and print
        if(new_Goal):
            print('Yes')
            return
            
        new_Med_list = list(new_Med)
        new_Med_list.sort(reverse=True)
        Start.clear()
        for i in new_Med_list:
            Start.append(Med.pop(i)) 
    print('No')

if __name__ == "__main__":
    function()