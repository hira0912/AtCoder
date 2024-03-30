from math import gcd
def function():
    A,B,C = map(int,input().split())
    v_gcd = gcd(A,B)
    v_gcd = gcd(v_gcd,C)

    print(A//v_gcd + B//v_gcd + C//v_gcd -3)

if __name__ == "__main__":
    function()