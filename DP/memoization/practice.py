n = int(input())
dp = [x for x in range(n+1)]
trace = [x for x in range(n+1)]
dp[1]=0
trace[1]=0

for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    trace[i]=i-1
    
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i] = dp[i//3]+1
        trace[i]=i//3
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i] = dp[i//2]+1
        trace[i]=i//2
    
print(dp[n])
print(n, end=" ")
back = n

while trace[back]!=0:
    print(trace[back], end=" ")
    back = trace[back]
        