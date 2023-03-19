testcase=int(input())


dp=[0 for x in range(11)]
dp[1]=1
dp[2]=2
dp[3]=4
def is_zero(n,goal):
    print(dp)
    if dp[n]!=0 and n==goal:
        return dp[n]
    else:
        if dp[n-1]*dp[n-2]*dp[n-3]!=0:
            dp[n]=dp[n-1]+dp[n-2]+dp[n-3]
            is_zero(n+1,goal)
            return
        else:
            is_zero(n-1,goal)
            return
        
        
    
for _ in range(testcase):
    n = int(input())
    if n<=3:
        print(dp[n])
    else:
        is_zero(n,n)
        print(dp)
            
        
    
    
