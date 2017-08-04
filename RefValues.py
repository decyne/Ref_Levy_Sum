class RefValues:
	def __init__(self):
		self.levy = 0

	# If the thing added to RefValues is another Refvalues then add each value together, otherwise 
  # add the int to every value
	def __add__(self,other):
		print(self.levy)
		print(other)
		print(self.__class__)
		if isinstance(other, self.__class__):
			self.levy + other.levy
		elif isinstance(other, int):
			self.levy + other
		else:
			raise TypeError("Unsupported operator type")	

		return self.levy
