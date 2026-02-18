N=int(input())
results=[]

for i in range(N):
    nums=list(map(int, input().split()))
    
    if nums[0]==nums[1] and nums[1]==nums[2] and nums[2]==nums[3]:
        results.append("YES")
    else:
        results.append("NO")
        
print(" ".join(map(str, results)))