#  Author	: BerkN
#  Date		: 20.09.2024 14:34

# Test Application

import os
import sys
sys.path.append('./')

from arlib import *

if __name__ == '__main__':

	cal = ARCalendar()
	cal.load('calendar.csv')

	sch = ARScheduler()
	sch.setCourses(cal.programs)

	# This function specifies the unique requirements for your calendar
	# All calendar combinations are tested in this check function. 
	def req(cal:ARCalendar):
		return (len(cal.getDays()) == 2) and (len(cal.programs) == 4)

	sch.schedule(req,ARCalendar())
	sch.printSelf()


