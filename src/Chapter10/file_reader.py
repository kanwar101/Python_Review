
with open("pi_digits.txt") as file:
	contents = file.read()
	print (contents.strip())

filename = "C:\\Users\\kanwa\\OneDrive\\Documents\\GitHub\\Python_Review\\src\\Chapter10\\pi_digits.txt"
with open(filename) as file_1:
	contents_1 = file_1.read()
	print (contents_1)


with open (filename) as file_2:
	for line in file_2:
		print (line.rstrip())
