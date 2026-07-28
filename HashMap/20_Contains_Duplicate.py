"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


            

print(Solution().containsDuplicate([1,2,3,4,6]))
                
        
"""
[ 1 , 2 , 3 , 4 , 5 ]
  <   >
  <       >
  <           >
  <               >
      <   >
      <       >
      <           >
          <   >  
          <       >
              <   >
  

"""
