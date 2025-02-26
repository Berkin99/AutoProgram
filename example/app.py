#  Author	: BerkN
#  Date		: 20.09.2024 14:34

# Test Application
# This functions specifies the unique requirements for your calendar
# All calendar combinations are tested in this check function. 
# Change the function for your calendar requirements, if calendar is as you wanted return True 

import sys
sys.path.append('./')

from arlib import *

# 5 lecture in only two days
def example1(cal:ARCalendar):
	days = cal.getDays()
	return (len(days) == 2 and len(cal.programs) >= 5)

# Maximum lecture, Two days (mon, tue)
def example2(cal:ARCalendar):
	days = cal.getDays()
	return (len(days) == 2 and days.__contains__("mon") and days.__contains__("tue"))

if __name__ == '__main__':

	#Load the programs to the scheduler
	sch = ARScheduler()
	sch.load('example/calendar.csv')

	sch.schedule(example2, ARCalendar())
	sch.printSelf()