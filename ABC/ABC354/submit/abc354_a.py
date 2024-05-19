def function():
    H = int(input())
    i = 0
    k = 0
    while True:
      k += 2**i
      i += 1
      if(H < k):
         print(i)
         break
    return

if __name__ == "__main__":
    function()