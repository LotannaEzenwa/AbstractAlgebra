from axiom import Axiom

class Set(object):
	"""
	A class definition for a Set object (Mathematical)
	While a lot of these are already defined by the python language,
	this is for both continuity and completeness. 

	This implements ZFC as defined in 
	https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
	"""
	def __init__(self,elements=None,rule=None):
		if (elements is not None) and (rule is not None):
			raise NotImplementedError("Set cannot be instantiated both elements and rule")

	


	

class Extensionality(Axiom):
	"""
	Defines the extensionality Axiom for set theory:
	Two sets are equal (are the same set) if they have the same elements.
	"""

	def __init__(self):
		pass


	def confirm(self,structure):
		raise NotImplementedError 