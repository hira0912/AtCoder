def function():
    x_a, y_a = map(int,input().split())
    x_b, y_b = map(int,input().split())
    x_c, y_c = map(int,input().split())

    d_ab = abs(x_a - x_b)**2 + abs(y_a - y_b)**2
    d_bc = abs(x_b - x_c)**2 + abs(y_b - y_c)**2
    d_ca = abs(x_c - x_a)**2 + abs(y_c - y_a)**2

    d = [d_ab,d_bc,d_ca]
    d.sort()

    if(d[2] == d[0]+d[1]):
        print('Yes')
    else:
        print('No')
    return

if __name__ == "__main__":
    function()