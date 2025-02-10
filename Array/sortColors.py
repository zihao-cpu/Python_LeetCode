def sortColors(self, nums: List[int]) -> None:
    # left 是0的右边界，right是2的左边界，index是指向当前数字。
    left, right, index = 0, len(nums) - 1, 0
    while index <= right:
        if nums[index] == 0:
            # 如果是0，就往前面移
            nums[left], nums[index] = nums[index], nums[left]
            left += 1
            index += 1
        elif nums[index] == 1:
            # 如果是1，不做任何交换
            index += 1
        elif nums[index] == 2:
            # 如果是2就往后面移
            nums[right], nums[index] = nums[index], nums[right]
            right -= 1
