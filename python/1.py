### 16 ms/13.4MB
### 暴力破解
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,nu in enumerate(nums):
            if target-nu in nums[i+1:]:
                result = [i,nums[i+1:].index(target-nu)+i+1]
                break
        return result
                
### java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0;i<nums.length-1;i++)
            for (int j=i+1;j<nums.length;j++)
                if (nums[j]==target-nums[i])
                {
                    int[] result = {i,j};
                    return result;
                }
        return new int[0];
    }
        
}
