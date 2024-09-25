#  Author	: BerkN
#  Date		: 20.09.2024 14:34

import os

from arlib.ardate import *
from arlib.arprogram import ARProgram
from arlib.arcalendar import ARCalendar

__author__ = 'BerkN'
__all__ = ['ARScheduler']

class ARScheduler:

	def __init__(self):
		self.courses:list[ARProgram] = []
		self.coursesLen = 0
		self.calendars:list[ARCalendar] = []
		self.iteration = 0

	def setCourses(self, pList:list[ARProgram]=[]):
		self.courses = pList
		self.coursesLen = len(pList)

	"""
	Scheduler looks for every possible calendar and checks it with
	the request function.
	@function request -> False is "not wanted", every other int
	describes quality level of calendar.
	"""
	def schedule(self, request, cal:ARCalendar = ARCalendar(), index=0):
		self.iteration += 1
		
		if index == self.coursesLen: #End of the tree -> test the request function:
			if request(cal) > 0:
				print("Found: " + str(self.iteration)) 
				self.calendars.append(cal.copy()) 
			return
		
		#Current Not Appended
		self.schedule(request, cal.copy(), index + 1) 
		if not cal.appendSafe(self.courses[index]): return #Return = no append counted already

		#Current Appended
		self.schedule(request, cal.copy(), index + 1)

	def printSelf(self):
		for i in range(len(self.calendars)):
			print("Calendar [{:d}]".format(i)) 
			self.calendars[i].printSelf()
	
	def export(self, path=""):
		os.mkdir('exports')
		for i in range(len(self.calendars)): self.calendars[i].save(path + "exports/calendar["+str(i)+"].csv")
	
