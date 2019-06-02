# Given a string S and a character C, return an array of integers
# representing the shortest distance from the character C in the string.
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


class Solution(object):
	def shortestToChar(self, S, C):
		prev = float('-inf')
		distance_to_chars = []
		for i, char in enumerate(S):	
			if char == C:
				prev = i
			distance_to_chars.append(i - prev)
		prev = float('inf')
		for i in reversed(xrange(len(S))):
			if S[i] == C:
				prev = i
			distance_to_chars[i] = min(distance_to_chars[i], prev - i)
		return distance_to_chars





























"""
		prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

"""