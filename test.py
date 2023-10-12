import os

# Get all environment variables as a dictionary
env_variables = os.environ

# Display all environment variables and their values
for key, value in env_variables.items():
    print(f'{key}: {value}')
