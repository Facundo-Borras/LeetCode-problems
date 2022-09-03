class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        not_found = True
        i = 0
        while not_found:
            one = nums[i]
            if one not in d.keys():
                d[one] = [i]
            else:
                d[one].append(i)
            if target-one in d.keys():
                if one == target-one and len(d[target-one]) > 1:
                    pos1 = d[target-one][0]
                    pos2 = d[target-one][1]
                    not_found = False
                elif one != target-one:
                    pos1 = d[target-one][0]
                    pos2 = i
                    not_found = False
            i += 1  
        return [pos1,pos2] 