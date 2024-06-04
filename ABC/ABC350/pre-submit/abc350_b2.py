import collections

# 標準入力及び配列の初期化
N,Q = map(int,input().split())
T = list(map(int,input().split()))

# collection.counterオブジェクトに格納
c = collections.Counter(T)
# Counter({'1': 4, '2': 2, '3': 1})

# collection.counterを順番に読む
for c_val in c.values():
    if(c_val%2==1):
        N -= 1

# 出力
print(N)