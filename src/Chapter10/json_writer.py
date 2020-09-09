import json as js

numbers = ['This', 'is','a','list','for', 'a','file']


filename = 'new_file.json'
with open (filename, 'a') as f:
	js.dump(numbers,f)

