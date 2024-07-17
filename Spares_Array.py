#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

sortedArray = []

def _merge(arr1, m, arr2, n):
    
    for x in arr1:
        if x != 0:
            sortedArray.append(x)
    for x in arr2:
        if x != 0:
            sortedArray.append(x)

_merge(nums1, 6, nums2, 3)

print(sortedArray)