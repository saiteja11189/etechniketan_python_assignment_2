s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

# Split the string into words
words = s1.split()

filtered_words = []

# Keep unique words of length >= 4 that start with 'w' or 'W'
for word in words:
    # Remove basic punctuation if present at the end of word
    cleaned_word = word.strip(",.?!")
    if len(cleaned_word) >= 4 and cleaned_word.lower().startswith('w'):
        if cleaned_word not in filtered_words:
            filtered_words.append(cleaned_word)

print(filtered_words)
