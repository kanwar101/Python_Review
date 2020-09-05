class Dog:
	"""working with classes"""

	def __init__(self,name,age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""give command to dog to sit"""
		print (self.name)

mydog = Dog("Tommy", 7)
mydog.sit()