def build_person(fname, lname, age=None):
	"""Returns Dictionary"""
	if age:
		persons ={"fname": fname, "lname": lname, 'age': age}
	else:
		persons = {"fname": fname, "lname": lname}
	return persons

print (build_person('Sam', 'Lewitt',34))


