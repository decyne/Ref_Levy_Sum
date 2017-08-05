class RefValues:
	def __init__(self):
		self.levy = 0

	# Returns a RefValues object with the same values
	def copy(self):
		copy_ref = RefValues()
		copy_ref.levy = self.levy
		return copy_ref

	# If the thing added to RefValues is another Refvalues then add each value together, otherwise 
  # add the int to every value
	def __add__(self,other):
		sum_ref = self.copy()
		if isinstance(other, self.__class__):
			sum_ref.levy = self.levy + other.levy
		elif isinstance(other, int):
			sum_ref.levy = self.levy + other
		else:
			raise TypeError("Unsupported operator type")	

		return sum_ref
