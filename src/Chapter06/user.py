
user_0 = {
	'username': 'sname',
	'first': 'Stuart',
	'last': 'Riley'
}

for user_key,user_value in user_0.items():
	print (f'User Key {user_key}')
	print (f'User Value {user_value}')



for user_key in user_0.keys():
	print ("Keys ONLY")
	print (f"USer Key {user_key}")

print ("***Values Only***")

for user_value in user_0.values():
	print (f"User Value {user_value}")

print ('***Values using Keys***')

for user_key in user_0.keys():
	print (f"User Value {user_0[user_key]}")




