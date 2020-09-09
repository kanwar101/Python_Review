class AnonymousSurvey:
	""" Get the Survey responses and print the same"""

	def __init__ (self, question):
		"""store a question"""
		self.question = question
		self.responses = []

	def show_question (self):
		"""print question """
		print (f"Question is: {self.question}")
	def store_response (self, response):
		"""store all the responses"""
		self.responses.append(response)


	def show_results (self):
		"""Print all the responses"""
		print ("Survey says :")
		for response in self.responses:
			print (f"{response}")


