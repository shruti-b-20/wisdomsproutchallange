def mergearrays(arr1,arr2):
    left=len(arr1)-1
    right=0
    while left>=0 and right<len(arr2):
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
ans=mergearrays(arr1,arr2)
print(arr1,arr2)