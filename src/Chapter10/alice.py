
def count_words(filename):
	try:
		with open (filename, encoding='UTF-8') as f:
			contents = f.read()
	except Exception as e:
		#print (f"Exception is {e}")
		pass
	else:
		length_of_the_file = len (contents)
		content_list = contents.split()
		print (f"Number of words is {len(content_list)}")

list_of_books = ['alice.txt','little_women.txt','try,txt']
for list in list_of_books:
	count_words(list)
