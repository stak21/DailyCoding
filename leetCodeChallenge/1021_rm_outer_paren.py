"""
	Remove the outer parenthesis of every primitive string in the primitive decomposition of s
	@s: A string of valid parenthesis and other chracters
"""

def removeOuterParenthesis(S: str) -> str:
	ret_str, counter = '', 0
	for c in S:
		if c == '(':
			counter += 1
		if counter > 1:
			ret_str += c
		if c == ')':
			counter -= 1

	return ret_str

    """ alternative method 
      def removeOuterParentheses(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)
   """


ex1 = "(())(()())"
print(removeOuterParenthesis(ex1))
