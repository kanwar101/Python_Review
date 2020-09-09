
def get_formatted_name (first, last, middle =''):
	"""Print formatted name"""

	if middle:
		return f"{first} {middle} {last}"
	else:
		return f"{first} {last}"


