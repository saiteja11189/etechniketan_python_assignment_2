# List of strings to check
words = ["aba", "xyz", "1991", "a", "radar", "hello", "noon", "ab"]

palindrome_count = 0

# Count strings that have length > 2 and are palindromes using slicing
for word in words:
    if len(word) > 2 and word == word[::-1]:
        palindrome_count += 1

print(f"List of words: {words}")
print(f"Number of palindromes with length > 2: {palindrome_count}")
