n = int(input()) #입력을 받자 일단
dp=[i for i in range(n+1)]
dp[1]=0 #즉, 아직 아무일도 일어나지않음
history = [i for i in range(n+1)]
history[1]=0

for i in range(2,n+1):
    dp[i] = dp[i-1]+1 #왜냐 2에서 3으로 가면적어도 1을 더하는 연산을 했다고 생각해서 더하기를 미리해줌
    history[i] = i-1 #적어도 바로 -1전에 꺼에서 흔적을 남겼을 테니가
    
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i]=dp[i//3]+1
        history[i]=i//3
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i]=dp[i//2]+1
        history[i]=i//2
print(dp[n])
print(n, end=" ")

back_num = n
while history[back_num] != 0:
    print(history[back_num],end=' ')
    back_num=history[back_num]
    
    
