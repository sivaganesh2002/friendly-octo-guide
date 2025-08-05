def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string can always be segmented

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

# Input reading
s = input().strip()
wordDict = input().strip().split()
# Output result as 'true' or 'false' (lowercase as per most problem statement conventions)
print(str(word_break(s, wordDict)).lower())