def findMedianSortedArrays(nums1, nums2):
    joined = nums1 + nums2
    joined.sort()
    middle = joined[len(joined) // 2]

    if len(joined) % 2 == 1:
        return middle
    else:
        middle2 = joined[len(joined) // 2 - 1]
        return (middle2 + middle) / 2.0


print(findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
