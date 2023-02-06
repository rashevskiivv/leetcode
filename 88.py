def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    while len(nums1) != m:
        nums1.pop()
    while len(nums2) != n:
        nums2.pop()
    for i in range(len(nums2)):
        nums1.append(nums2[i])
    nums1.sort()


if __name__ == '__main__':
    print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))