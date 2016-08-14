from abc import ABCMeta, abstractmethod
from types import {
	FunctionType,
	LambdaType,
	GeneratorType,
}

class Axiom(metaclass=ABCMeta):
	"""
	A base class for axioms
	"""
	rule_types = [FunctionType,LambdaType,GeneratorType]
	def __init__(self, rule=None):
		if not any(isinstance(rule,rule_type) for rule_type in rule_types):
			raise ValueError("Rule %s not function or generator" % str(rule))
		self._rule = rule

	@abstractmethod
	def confirm():
		"""
		Classes should implement this as a static method
		"""
		raise NotImplementedError