# Read string from user
s1 = input("Enter a string: ")

char_count = {}

# Count character appearances
for char in s1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the resulting character frequency dictionary
print("Character appearance counts:")
print(char_count)
