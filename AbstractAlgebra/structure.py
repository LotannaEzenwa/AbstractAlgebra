from abc import ABCMeta, absractproperty

class Structure(metaclass=ABCMeta):
	"""
	An Abstract Base Class for an Algebraic Structure
	Defined as in https://en.wikipedia.org/wiki/Algebraic_structure

	Each Structure has both a set and a mathematical object attached to it
	"""
	def __init__(self, set_obj, math_obj):
		pass

