def function():
    # 標準入力
    N = int(input())
    A = list(map(int,input().split()))

    # 排他的論理和の値のsetを作成
    B = set()
    B.add(xor(A))

    # 全探索後の結果のsetと合成
    B.union(calc(A,B))
    print(len(B))
    return

# 再帰関数
def calc(A:list,B:set)->set:
    if(len(A)<2):
        B.add(xor(A))
        return B
    B.add(xor(A))
    # 移動元と移動先の探索
    for i in range(len(A)):
        for j in range(len(A)):
            if(i!=j):
                A_dup = list(A)
                A_dup[i] += A_dup[j]
                # 移動元配列の削除
                del A_dup[j]
                B.add(xor(A))
                if(len(A)>=2):
                    B.union(calc(A_dup,B))
    return B

# 配列の排他的論理和を求める
def xor(A:list)->int:
    ret = A[0]
    for i in range(1,len(A)):
        ret = ret^A[i]
    return ret

if __name__ == "__main__":
    function()