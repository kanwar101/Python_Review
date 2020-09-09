import json 

filename = 'new_file.json'
with open (filename) as f:
	numbers = json.load(f)


print (numbers)