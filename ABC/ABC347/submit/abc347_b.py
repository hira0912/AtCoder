def function():
    S = str(input())
    S_set = set()
    for i in range(len(S)):
        for j in range(len(S)-i):
            if not S[j:j+i+1] in S_set:
                S_set.add(S[j:j+i+1])

    print(len(S_set))


if __name__ == "__main__":
    function()