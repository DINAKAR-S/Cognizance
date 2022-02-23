# Write a program to accept a string from the user and display characters, that are present at an even index number.

string = input('Enter a string: ')
even_chars = []

for i in range(len(string)):
    if i % 2 == 0:
        even_chars.append(string[i])
print('Even index characters: {}'.format(even_chars))