class Set(object):
	"""
	A class definition for a Set object (Mathematical)
	While a lot of these are already defined by the python language,
	this is for continuity.
	"""
	def __init__(self,elements=None,rule=None):
		if (elements is not None) and (rule is not None):
			raise NotImplementedError("Set cannot be instantiated both elements and rule")

		pass

	

