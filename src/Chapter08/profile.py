
def build_profile (first, last, **dictionary):
	"""This dictionary contains everything about thge user"""
	dictionary['first_name'] = first
	dictionary['last_name'] = last

	return dictionary

print (build_profile ('tom', 'serin', location='NJ', firm='citi'))