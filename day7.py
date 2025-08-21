def trappedwater(arr):
    leftmax,rightmax,total=0,0,0
    left=0
    right=len(arr)-1
    while left < right:
        if arr[left]<=arr[right]:
            if leftmax > arr[left]:
                total+=leftmax-arr[left]
            else:
                leftmax=arr[left]
            left+=1
        else:
            if rightmax > arr[right]:
                total+=rightmax-arr[right]
            else:
                rightmax=arr[right]
            right-=1
    return total
#TESTCASES
print("Input: [0,1,0,2,1,0,1,3,2,1,2,1] → Output:", trappedwater([0,1,0,2,1,0,1,3,2,1,2,1]))
print("Input: [4,2,0,3,2,5] → Output:", trappedwater([4,2,0,3,2,5]))
print("Input: [1,1,1] → Output:", trappedwater([1,1,1]))
print("Input: [5] → Output:", trappedwater([5]))
print("Input: [2,0,2] → Output:", trappedwater([2,0,2]))