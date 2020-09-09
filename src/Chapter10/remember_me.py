import json

user_input = input ("What is your name: ")

filename = 'new_file.json'

with open (filename, 'w') as f:
	json.dump (user_input, f)

print (filename)