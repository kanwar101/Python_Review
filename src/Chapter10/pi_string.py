
filename = "C:\\Users\\kanwa\\OneDrive\\Documents\\GitHub\\Python_Review\\src\\Chapter10\\pi1000000.txt"

with open (filename) as file_pointer:
	all_lines = file_pointer.readlines()
	#print (all_lines)

pi_string =""

for line in all_lines:
	pi_string += line.strip()

print (pi_string [:52])
print (len(pi_string))

search_num='592365734822356'

if search_num in pi_string:
	print (f"String {search_num} is present in pi million")

else:
	print (f"String {search_num} is NOT THERE")