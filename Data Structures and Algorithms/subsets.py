class Solution:
	def subsets(self, nums):
		ans = []
		def helper(start,curr):
			ans.append(curr.copy())
			for i in range(start, len(nums)):
				tmp = curr.copy()
				tmp.append(nums[i])
				helper(i+1,tmp)
				tmp.pop()
		helper(0,[])
		return ans


s = Solution()
print(s.subsets([1,2,3]))
# print(Solution.subsets([1,2,3]))