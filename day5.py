def leaders(arr):
    curl=arr[-1]
    n=len(arr)
    ans=[]
    ans.append(curl)
    for i in range(n-2,-1,-1):
        if curl<=arr[i]:
            curl=arr[i]
            ans.append(arr[i])
    return ans[::-1]


# TESTCASES
print(leaders([16, 17, 4, 3, 5, 2]))       
print(leaders([1, 2, 3, 4, 0]))           
print(leaders([7, 10, 4, 10, 6, 5, 2]))    
print(leaders([5]))                        
print(leaders([100, 50, 20, 10]))          
print(leaders([61, 61, 17]))               
print(leaders(list(range(1, 1000001))))    

