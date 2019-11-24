# replace with alphabet position
# Requirements:
#   Return a string where all the letters have been replaced with their
#   corresponding number position
#   non letter strings are skipped
#   iterate through the whole string
#   use ord to get the char from ascii
# Input: "abc"
# Process:
#   for each char in string:
#   add to the list the position number by using ord 
#   make sure that the char is lowercase
#   make sure that the char is a letter
#   join the list into a string and return the string

# Output: "1 2 3"

def alpha_positions(s: str) -> str:
    print(s)
    positions = [str(ord(c.lower()) - 96) for c in s if c.isalpha()]
    return ' '.join(positions)

print((alpha_positions("a") == "1"))
print((alpha_positions("ab") == "1 2"))
print((alpha_positions("a b") == "1 2"))
print((alpha_positions("a c") == "1 3"))
print((alpha_positions("a d e f") == "1 4 5 6"))
