def function():
    NEWS = ['N','E','W','S']
    SWEN = ['S','W','E','N']

    D = str(input())

    for i in range(len(D)):
        for k in range(4):
            if(D[i]==NEWS[k]):
                D = D[:i] + SWEN[k] + D[i+1:]
                break
    print(D)

if __name__ == "__main__":
    function()