i = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ', ']
for x in range(len(i)):
    with open('webinar.txt', 'r') as f:
        old_file = f.read()
        new_file = old_file.replace(i[x], '')
    with open('webinar.txt', 'w') as f:
        f.write(new_file)
print(new_file)