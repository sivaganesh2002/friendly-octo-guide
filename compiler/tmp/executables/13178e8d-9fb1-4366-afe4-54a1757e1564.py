def wordcheck(s, wl):
    wl = set(wl)
    n = len(s)
    
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wl:
                dp[i] = True
                break

    dp[n];

s = input().strip()
wordDict = input().strip().split()

print(wordcheck(s, wordDict))