#  Author	: BerkN
#  Date		: 20.09.2024 14:34

from arlib.ardate import *

__author__ = 'BerkN'
__all__ = ['ARProgram']

class ARProgram:
	"""
	* name		: unique string ex: "MATH101"
	* priority	: credit 
	* dates		: list of ARDate
	"""
	def __init__(self, name: str, priority = 1, dates = []):
		self.name				= name
		self.priority			= priority
		self.dates:list[ARDate]	= []
		self.days				= 0x00
		for date in dates: self.append(date)

	def append(self, date:ARDate) -> bool:
		if not date.isValid(): return False
		for sdate in self.dates:
			if sdate == date:
				print(self.name + "> can't append intersecting dates : " + date.getString()) 
				return False  
		self.dates.append(date)
		self.days |= 0x01 << date.Iday		
		return True

	def isIntersect(self, other: object) -> bool:
		for sdate in self.dates:
			for odate in other.dates:
				if sdate == odate: return True
		return False
	
	def getDays(self):
		return ARClass.binaryDay(self.days)
	
	def getString(self):
		s = self.name + " " + str(self.priority)
		for date in self.dates: s += " " + date.getString()
		return s
	
	def getDuration(self) -> int:
		d = 0
		for date in self.dates: d += date.getDuration()
		return d

	def __lt__(self, other: object) -> bool: return self.priority < other.priority
	def __gt__(self, other: object) -> bool: return self.priority > other.priority
	def __eq__(self, other: object) -> bool: 
		if type(other) != type(self): return False 
		return self.priority == other.priority

def isIntersect(prog1:ARProgram, prog2:ARProgram) -> bool:
	return prog1.isIntersect(prog2)
