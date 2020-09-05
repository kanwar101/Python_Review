print ("Please give 2 numbers to divide: ")
print ("Press q to exit")

while True:
	first_num = input ("First number: ")
	if first_num=='q':
		break
	second_num = input ("Second numbe: ")
	if second_num =='q':
		break
	try:
		answer = int(first_num)/int(second_num)
	except Exception as e:
		print (e)
	else:
		print (answer)