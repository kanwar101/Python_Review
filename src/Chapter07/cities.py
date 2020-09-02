prompt = 'Enter the name of the city you visited'

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print (f"City is {city}")