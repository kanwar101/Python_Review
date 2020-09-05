
class Car:
	"""Car Class"""
	def __init__ (self, make, model, year):
		"""initializing the class"""
		self.car_make = make
		self.car_model=model
		self.car_year = year

	def show_car_description (self):
		"""Print Car details"""
		print (f"Car make is {self.car_make} and model is {self.car_model} and is made in {self.car_year}")

class Battery:
	"""Battery Class to get size of Battery"""

	def __init__ (self, battery_size=100):
		"""initializing the class battery"""
		self.battery_size=battery_size

	def describe_battery (self):
		"""this function is going to print the battery size"""
		print (f"Battery size is {self.battery_size}")

class ElectricCar (Car):
	"""Electric Car description"""
	def __init__ (self, make,model,year):
		"""initializing the parent class"""
		super().__init__(make, model, year)
		self.battery=Battery()

electric_car_inst = ElectricCar('tesla','t3', '2018')
electric_car_inst.battery.describe_battery()



