# Determine whether an integer is a palindrome.
def isPalindrome(x):
	y = [ch for ch in str(x)]
	return list(reversed(y)) == y

# Return the index if the target exists. If not, return the index where it would be.
def searchInsert(nums, target):
	return nums.index(target) if target in nums else len(filter(lambda x: x < target, nums))
