import numpy as np

def function():
    H,W = map(int,input().split())
    data = []
    for i in range(H):
        data.append(list(map(int,input().split())))
    
    sum_h = list(map(int,np.sum(data,axis=1)))
    sum_w = list(map(int,np.sum(data,axis=0)))
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = sum_h[i] + sum_w[j] - data[i][j]
        data_str = str(data[i]).replace(',','')[1:-1]
        print(data_str)
        
if __name__ == "__main__":
    function()