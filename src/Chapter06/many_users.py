users = {
	'aeinstein' : {'fname': 'albert', 'lname': 'einstein', 'location':'princeton','car':'Ford'},
	'mcurie': {'mname':'marie', 'lname':'curie', 'location':'paris'}
}


for user_key, user_value in users.items():
	print (f"{user_key} details are")
	for sub_user_key, sub_user_value in user_value.items():
		print (f"{sub_user_key} is {sub_user_value}" )