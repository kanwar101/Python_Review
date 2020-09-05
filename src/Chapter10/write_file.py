filename='output.txt'
with open (filename, 'a') as file_op:
	file_op.write ("Write into output file")
	print (file_op.write ("\nAdding new line"))