s1 = 'practice is important to perfectly learn python'

# Find all indexes of 'p' in the string
indexes = []
for index, char in enumerate(s1):
    if char == 'p':
        indexes.append(index)

# Print the final list of indexes
print(indexes)
