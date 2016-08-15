from axiom import Axiom

class Set(object):
	"""
	A class definition for a Set object (Mathematical)
	While a lot of these are already defined by the python language,
	this is for both continuity and completeness. 

	This implements ZFC as defined in 
	https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
	"""
	def __init__(self,elements=None,axioms=None):
		if (elements is not None) and (rule is not None):
			raise NotImplementedError("Set cannot be instantiated both elements and rule")

	def __iter__(self)
		return self

	def next(self):
		raise NotImplementedError

	

class Extensionality(Axiom):
	"""
	Defines the extensionality Axiom for set theory:
	Two sets are equal (are the same set) if they have the same elements.

	Implemented as Structure implements "Equals"
	"""
	def __init__(self, structure=None):

	@classmethod
	def override_equals(cls):
		raise NotImplementedError

	@staticmethod
	def confirm(structure):
		return 

class Regularity(Axiom):
	"""
	Defines the Regularity Axiom for set Theory:
	Every non-empty set x contains a member y such that x and y are disjoint sets.


	"""

	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class Specification(Axiom):
	"""
	Defines the Axiom of Schema Specification:
	Elements of a Set can be specified using a rule


	Implemented as structure implements "generator"
	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class Pairing(Axiom):
	"""
	Defines the Axiom of Pairing:
	If x and y are sets, then there exists a set which contains x and y as elements.
	(Implemented that two sets can be elements of another set)


	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class Union(Axiom):
	"""
	Defines the Axiom of Union:
	Given any set A, there is a set B such that, for any element c, c is a member of B if and only if there is a set D such that c is a member of D and D is a member of A.
	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class Replacement(Axiom):
	"""
	Defines the Axiom Schema of Replacement:
	The axiom schema of replacement asserts that the image of a set under any definable function will also fall inside a set.

	Functions on some structure must return a valid structure
	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class Infinity(Axiom):
	"""
	Defines the Axiom of Infinity:
	A set an be built be having an empty set unioned with y unioned with a set containing itself.
	Or, There exists a set having infintely many members

	Structure can implement an infinite generator
	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

class PowerSet(Axiom):
	"""
	Defines the Axiom of the Power Set:
	The Axiom of Power Set states that for any set x, there is a set y that contains every subset of x:


	"""
	def __init__(self):
		pass

	@staticmethod
	def confirm(structure):
		raise NotImplementedError

		

