def removeDuplicateLetters(s):
    # Initialize a stack to store characters in lexicographical order
    stack = []

    # Create a dictionary to keep track of character frequencies in the string
    char_count = {}

    # Create a set to check if a character is already in the stack
    in_stack = set()

    # Count character frequencies
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the string
    for char in s:
        # Decrement the count of the current character
        char_count[char] -= 1

        # Skip characters that are already in the stack
        if char in in_stack:
            continue

        # Pop characters from the stack if they are greater than the current character
        while stack and char < stack[-1] and char_count[stack[-1]] > 0:
            removed_char = stack.pop()
            in_stack.remove(removed_char)

        # Append the current character to the stack
        stack.append(char)
        in_stack.add(char)

    # Convert the stack to a string and return the result
    return ''.join(stack)

# Example usage:
s = "bcabc"
result = removeDuplicateLetters(s)
print(result)  # Output: "abc"