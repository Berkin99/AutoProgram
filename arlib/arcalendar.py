#  Author	: BerkN
#  Date		: 20.09.2024 20:13

import csv
from arlib.arprogram import ARProgram
from arlib.ardate import ARDate
from arlib.ardate import ARClass

__author__ = 'BerkN'
__all__ = ['ARCalendar']

class ARCalendar:
	def __init__(self):
		self.programs : list[ARProgram] = []
		self.days = 0     #Binary week marking

	def removeQuery(self, query):
		i = 0
		while i < len(self.programs):
			if query(self.programs[i]): self.programs.pop(i)
			else: i += 1
		self.updateDays()

	"""
	Append programs with intersection control 
	"""
	def appendSafe(self, prog:ARProgram) -> bool:
		if self.isIntersect(prog): return False
		self.append(prog)
		return True

	def append(self, prog:ARProgram):
		self.programs.append(prog)
		self.days |= prog.days

	def copy(self):
		new = ARCalendar()
		new.programs = self.programs.copy()
		new.updateDays()
		return new
		
	def isIntersect(self, prog:ARProgram) -> bool:
		for p in self.programs:
			if p.isIntersect(prog): return True
		return False

	def contains(self, prog:ARProgram) -> bool:
		for p in self.programs:
			if p.name == prog.name: return True
		return False

	def controlSelf(self) -> bool:
		plen = len(self.programs)
		for i in range(plen - 1):
			j = i + 1
			while j < plen:
				if self.programs[i].isIntersect(self.programs[j]): return False
				j += 1
		return True
	
	"""
	Sum priority of the programs in the calendar. 
	"""
	def getPrisum(self):
		i = 0 
		for prog in self.programs: i += prog.priority
		return i
	
	"""
	Occupied days list.
	"""
	def getDays(self) -> list[str]: return ARClass.binaryDay(self.days)

	def updateDays(self):
		self.days = 0
		for p in self.programs: self.days |= p.days

	def printSelf(self): 
		for prog in self.programs: print(prog.getString())

	def load(self, filename = 'calendar.csv'):
		with open(filename, 'r', newline='') as file:
			reader = csv.reader(file)
			for row in reader:
				rl = len(row)
				if rl < 5: break
				prog = ARProgram(row[0], row[1])
				i = 2
				while (rl - i - 1 / 3) > 0:
					prog.append(ARDate(row[i], row[i+1], row[i+2]))
					i += 3
				self.append(prog)

	def save(self, filename = 'calendar.csv'):
		with open(filename, 'w', newline='') as file:
			writer = csv.writer(file)
			for prog in self.programs:
				row  = prog.getString().split()
				writer.writerow(row)
