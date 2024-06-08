def function():
    N = int(input())
    mond = 998244353
    Nmond = N % mond
    Kmond = Nmond
    for _ in range(N):
        vKmond = str(Kmond) + str(Kmond)
        Kmond = int(vKmond) % mond
    print(Kmond)

if __name__ == "__main__":
    function()