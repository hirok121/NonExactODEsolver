import os

# Get all environment variables as a dictionary
env_variables = os.environ

<<<<<<< HEAD
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
    #by ssh key
=======
# Display all environment variables and their values
for key, value in env_variables.items():
    print(f'{key}: {value}')
>>>>>>> e0467557a2fec24b9c6a008230b412b0e3c52675
