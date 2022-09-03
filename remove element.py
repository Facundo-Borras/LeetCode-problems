class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        last = -1
        k = len(nums)
        for n in range(len(nums)):
            if nums[n] == val:
                not_found = True
                while abs(last) <= len(nums) and not_found:
                    if nums[last] == val:
                        nums[last] = "_"
                        k -=1
                    if  nums[n] == val and nums[last] != "_" and nums[last] != val:
                        not_found = False
                        nums[n] = nums[last]
                        nums[last] = "_"
                        k -=1
                    else:
                        last -= 1 
        return k