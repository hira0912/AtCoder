def function():
    S = sorted(input())
    s_save = ''
    s_count = 0

    str_i = []
    for i in range(101):
        str_i.append('') 
    
    for c in S:
        if(c != s_save):
            if(s_count != 0):
                str_i[s_count] += s_save
            s_count = 0
            s_save = c
        s_count += 1
    if(s_count != 0):
        str_i[s_count] += s_save

    for i in range(101):
        if(len(str_i[i]) != 0 and len(str_i[i]) != 2):
            print('No')
            return
    
    print('Yes')
    return


if __name__ == "__main__":
    function()