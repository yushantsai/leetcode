# Determine whether an integer is a palindrome.
def isPalindrome(x):
	y = [ch for ch in str(x)]
	return list(reversed(y)) == y

# Return the index if the target exists. If not, return the index where it would be.
def searchInsert(nums, target):
	return nums.index(target) if target in nums else len(filter(lambda x: x < target, nums))

# Merge two sorted linked lists and return it as a new one.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def mergeTwoLists(l1, l2):
	if l1 is None:
		return l2
	if l2 is None:
		return l1
	if l1.val < l2.val:
		l1.next = mergeTwoLists(l1.next, l2)
		return l1
	else:
		l2.next = mergeTwoLists(l1, l2.next)
		return l2

# Given an integer n, and generate the n-th count-and-say sequence.
def countAndSay(n):
	val = "1"
	if n > 1:
		for i in range(1, n + 1):
			tmp = val
			val = ""	# Clear the sequence.
			ch = tmp[0]	# Start with the 1st character.
			cnt = 1	# Set the counter.
			for j in range(1, len(tmp)):
				if tmp[j] == ch:	# if two adjacent characters are the same, increase the value of the counter.
					cnt += 1
				else:	# If not, update the sequence and reset the counter.
					val += str(cnt)
					val += ch
					ch = tmp[j]
					cnt = 1
				# Update the sequence.
				val += str(cnt)
				val += ch
	return val

# Calculate the hamming distance between two integers.
def hammingDistance(x, y):
	return bin(x ^ y).count("1")

# Determine whether the usage of capitals in a word is right or wrong.
def detectCapitalUse(word):
	return word.istitle() or word.isupper() or word.islower()

# Get unique elements in the intersection of two lists.
def intersection(nums1, nums2):
	return list(set(nums1) & set(nums2))

# Determine two binary tree are equal.
def isSameTree(p, q):
        if p and q:
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        return p is q