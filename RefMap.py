from RefValues import RefValues

class RefMap:
	
	REF_LEVY=5
	ASSESS_LEVY=-25

	def __init__(self,name):
		self.rmap={}
		self.name=name

	# Increment the referee's levies
	def _incLevy(self, name, amount):
		if name in self.rmap:
			# If the referee already exists increment the levies
			attributes = self.rmap[name]
			attributes.levy = attributes.levy + amount
		else:
			# Otherwise create the referee and increment the initial levy 
			new_attributes = RefValues()
			new_attributes.levy = amount
			self.rmap[name] = new_attributes	

	# Combines two dictionaries together and sums any common keys
	def _combineDict(self, dict1, dict2):
		sum_dict = dict1.copy()
		
		# Loop over all keys in dict2 and add them to the dict1 copy
		for key, val in dict2.items():
			if key in sum_dict:
				# If it existed in dict1 originally add them together
				sum_dict[key] = sum_dict[key] + val
			else:
				# Otherwise just put the value straight into dict1 copy
				sum_dict[key] = val.copy()

		return sum_dict	

	def incReferee(self, referee):
		self._incLevy(referee,self.REF_LEVY)

	def incAssessor(self, assessor):
		self._incLevy(assessor,self.ASSESS_LEVY)

	# Return the levies owed for this referee
	def getLevy(self, referee):
		try:
			attributes = self.rmap[referee]
			return attributes.levy
		except KeyError:
			return 0

	def printLevy(self):
		for name in self.rmap:
			levy = self.rmap[name].levy
			print(name, levy)

	# Creates a RefMap with concatonaed referees, any common referees have their values summed
	def __add__(self,other):
		# Python sum function adds dictionary to 0 initially, need to create a case to allow for that
		if (other == 0):
			return self
		summed_refmap = RefMap("Merged")
		summed_refmap.rmap = self._combineDict(self.rmap, other.rmap)
		return summed_refmap

	# Define reverse add to have the same functionality as add
	__radd__ = __add__
