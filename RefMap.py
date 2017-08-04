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

	def __add__(self,other):
		summed_refmap = RefMap("Merged")
		summed_refmap.rmap = other.rmap.copy()
		
		try:
			
		return summed_refmap
