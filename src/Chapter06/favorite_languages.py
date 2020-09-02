favorite_language={
	'Bob': 'python',
	'Dan': 'C',
	'Steve': 'Java',
	'Reddy': 'Ruby'
}

print (favorite_language.get('stuart','Who Stuart?'))

favorite_language= {
	'Bob': ['python', 'C', 'R'],
	'Dan': ['Java', 'C++']
}


for user_name, user_languages in favorite_language.items():
	print (f"User {user_name} knows below languages")
	for user_lang in user_languages:
		print (user_lang)

print ("END")

