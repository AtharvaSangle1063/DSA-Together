#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        sumarr=0
        sum=0
        
        for i in range(1,n+1):
            sum+=i
        
        for j in range(0,n-1):
            sumarr+=array[j]
        return sum-sumarr
    
            
           
        
                
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
