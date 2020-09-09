import json


def get_existing_user():
	"""get user name if available"""
	filename = 'new_file2.json'
	try:
		with open (filename) as f:
			name = json.load(f)
	except Exception as e:
		return None
	else:
		return name

def greet_user ():
	""" Greet user"""
	user_name = get_existing_user()
	if user_name:
		print (f"Welcome Back : {user_name}")
		
	else:
		create_new_user()

def create_new_user():
	""" Create new user if user does not exist"""
	text_input = input("what is your name: ")
	filename = 'new_file2.json'
	with open (filename,'w') as f:
		json.dump(text_input, f)
		print (f"USER NAME is: {text_input}")


greet_user()