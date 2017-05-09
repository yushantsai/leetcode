# Determine whether an integer is a palindrome.
def isPalindrome(x):
	y = [ch for ch in str(x)]
	return list(reversed(y)) == y

