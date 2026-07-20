d = {
    'name': 'Kelly', 
    'age': 25, 
    'salary': 8000, 
    'city': 'New york'
}
keys_to_remove = ['name', 'salary']

# Remove the specified keys
for key in keys_to_remove:
    if key in d:
        d.pop(key)

print(d)
