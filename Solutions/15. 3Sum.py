class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    while l < r:
                        l += 1
                        if nums[l-1] != nums[l]:
                            break

                elif nums[i] + nums[l] + nums[r] > 0:
                    while r > l:
                        r -= 1
                        if nums[r+1] != nums[r]:
                            break
                else:
                    triplets.append([nums[i], nums[r], nums[l]])
                    while l < r:
                        l += 1
                        if nums[l-1] != nums[l]:
                            break
            while i < len(nums) - 2:
                i += 1
                if nums[i - 1] != nums[i]:
                    break

        return triplets