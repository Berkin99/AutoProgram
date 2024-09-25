#  Author	: BerkN
#  Date		: 20.09.2024 14:34

# Test Application

import os
import sys
sys.path.append('./')

from arlib import *

if __name__ == '__main__':

	#Load the programs to the scheduler
	sch = ARScheduler()
	sch.load('calendar.csv')

	# This function specifies the unique requirements for your calendar
	# All calendar combinations are tested in this check function. 
	# Change this function for your calendar requirements, if calendar is as you wanted return True 
	def req(cal:ARCalendar):
		return (len(cal.getDays()) == 2) and (len(cal.programs) == 5)

	sch.schedule(req,ARCalendar())
	sch.printSelf()


