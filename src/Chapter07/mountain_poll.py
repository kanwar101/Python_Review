

responses = {}

polling_active = True

while polling_active:
	name = input ("Your Name Please\n")
	response = input ("Did you Vote Yet\n")

	responses[name]=response

	repeat = input ("Do you Want to Continue")

	if repeat == 'No':
		polling_active=False

print ("Results are: ")

for user_key, user_value in responses.items():
	print (f"User Name is {user_key} and Voting Response is  {user_value}")

