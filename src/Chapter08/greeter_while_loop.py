
def get_formatted_name (fname, lname):
	""" Gives formatted name"""
	formatted_name = f"{fname} {lname}"
	return formatted_name

while True:
	print ("Please enter your name: ")
	f_name = input("First Name: ")
	l_name = input("Last Name: ")
	print (get_formatted_name(f_name,l_name))
	print ("Do You Want to Continue: ")
	cont = input("Y/N: ")
	if cont == 'N':
		break