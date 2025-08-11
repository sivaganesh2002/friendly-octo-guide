import sys

# Get the input 'n' from the command line arguments
# The first argument (sys.argv[0]) is the script name itself,
# so we access sys.argv[1] for the user's input.
try:
    n = int(sys.argv[1])
except (IndexError, ValueError):
    # Handle cases where the user doesn't provide a number or provides an invalid one
    print("Please provide a valid integer as a command-line argument.")
    sys.exit()

result = []
for i in range(1, n + 1):
    # Check for divisibility by both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    # Then check for divisibility by 3
    elif i % 3 == 0:
        result.append("Fizz")
    # Then check for divisibility by 5
    elif i % 5 == 0:
        result.append("Buzz")
    # Otherwise, append the number as a string
    else:
        result.append(str(i))

# Print the final list as the output
print(result)