#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

sortedArray = []

def _merge(arr1, m, arr2, n):
    small1, small2 = 0, 0
    for y in arr1:
        for x in arr2:
            if x < y:
                sortedArray.append(x)
            elif x == y:
                sortedArray.append(x)
                sortedArray.append(y)
            else:
                sortedArray.append(y)


_merge(nums1, len(nums1), nums2, len(nums2))

print(sortedArray)