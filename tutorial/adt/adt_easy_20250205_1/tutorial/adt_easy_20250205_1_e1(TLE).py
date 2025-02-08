def function():
    N = int(input())

    val = 0
    cnt = 0
    while(cnt<N):
        val += 1
        if(val<10):
            cnt += 1
        else:
            val_str = str(val)
            flag = True
            for i in range(1,len(val_str)):
                if(int(val_str[i])>=int(val_str[i-1])):
                    flag = False
                    break
            if(flag):
                cnt += 1
                #print(val,cnt)
    print(val)
    return

if __name__ == "__main__":
    function()