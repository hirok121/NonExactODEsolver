import re

# Input string
input_string = "y(a)=b"

# Define a regular expression pattern to match 'a' and 'b'
pattern = r'y\((.*?)\)=(.*)'

# Use re.search to find the pattern in the input string
match = re.search(pattern, input_string)

# Check if a match was found
if match:
    a = match.group(1)  # Extract the value of 'a'
    b = match.group(2)  # Extract the value of 'b'
    print("a =", a)
    print("b =", b)
else:
    print("No match found")