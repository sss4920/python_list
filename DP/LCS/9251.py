sentence_a = input()
sentence_b = input()
row = len(sentence_a)
col = len(sentence_b)
dp = [[0]*(col+1) for _ in range(row+1)]

for y in range(row):
    for x in range(col):
        if sentence_a[y]==sentence_b[x]:
            dp[y+1][x+1] = dp[y][x]+1
        else:
            dp[y+1][x+1] = max(dp[y][x+1],dp[y+1][x])
print(dp[row][col])
        