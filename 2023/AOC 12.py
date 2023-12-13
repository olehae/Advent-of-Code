from functools import cache

with open('input12.txt') as f:
    lines = f.read().strip().split("\n")


@cache
def count(arr, nums):
    if arr == "":
        if nums == ():
            return 1
        else:
            return 0
    if nums == ():
        if "#" in arr:
            return 0
        else:
            return 1

    result = 0
    # treat ? as .
    if arr[0] in ".?":
        # move to right
        result += count(arr[1:], nums)

    # treat ? as #
    if arr[0] in "#?":
        # enough_springs_left = nums[0] <= len(arr)
        # no_dots_before = "." not in arr[:nums[0]]
        # next_is_dot = (nums[0] == len(arr) or arr[nums[0]] != "#")
        if nums[0] <= len(arr) and "." not in arr[:nums[0]] and (nums[0] == len(arr) or arr[nums[0]] != "#"):
            # block is finished -> +1 for the . after block and remove first element of nums
            result += count(arr[nums[0] + 1:], nums[1:])
        # else no more valid combinations

    return result


total1, total2 = 0, 0
for line in lines:
    arr1, nums1 = line.split()
    nums1 = tuple(map(int, nums1.split(",")))
    total1 += count(arr=arr1, nums=nums1)

    arr2 = "?".join([arr1] * 5)
    nums2 = nums1 * 5
    total2 += count(arr=arr2, nums=nums2)

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
