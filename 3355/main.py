'''shorten'''
nums = []

while True:
    n = int(input())

    if n == -1:
        break

    nums.append(n)

if len(nums) > 0:
    ans = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ans.append(str(start))
            else:
                ans.append(str(start) + "-" + str(nums[i - 1]))

            start = nums[i]

    if start == nums[-1]:
        ans.append(str(start))
    else:
        ans.append(str(start) + "-" + str(nums[-1]))

    print(", ".join(ans))
