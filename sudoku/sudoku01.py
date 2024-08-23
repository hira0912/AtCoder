def lambda_handler(event, context):
    
    panel_first = ['x91x65x7x','xx6xx48x1','xx5817x26','xxxxxxxxx','162x89xx4','4xx1xx68x','25xxx819x','6xxx513x2','xxx472xxx']
    panel_last = ['891265473','726394851','345817926','538746219','162589734','479123685','254638197','687951342','913472568']
    
    panel_ans = calc(panel_first)
    
    # TODO implement
    return panel_ans

def calc(panel):
    # 初期値の設定
    pos_x = 0
    pos_y = 0
    possibility = ['1','2','3','4','5','6','7','8','9']
    
def setpos(panel,pos_y,pos_x,possibility):
    while(possibility):
        if(pos_y==8 and pos_x=8):
            if(check_panel(panel)!=False)


def check_panel(panel):
    # 各行の調査    
    for i in range(9):
        ans = []
        for j in range(9):
            ans.append(panel[i][j])
        if(check_ans(ans)==False):
            return False
    
    # 各列の調査
    for j in range(9):
        ans = []
        for i in range(9):
            ans.append(panel[i][j])
        if(check_ans(ans)==False):
            return False
    
    # 各ブロックの調査
    for k in range(9):
        row = k // 3
        col = k % 3
        ans = []
        for l in range(9):
            x = l // 3
            y = l % 3
            ans.append(panel[3*row + x][3*col + y])
        if(check_ans(ans)==False):
            return False
    
# 特定9文字配列の確認
def check_ans(ans):
    checker = '123456789'
    ans.sort()
    ans_join = ''.join(ans)
    if(ans_join != checker):
        return False
    return True