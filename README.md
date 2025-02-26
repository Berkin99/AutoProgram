# **AUTOPROGRAM**

Autoprogram allows you to select the one that suits you best from alternative combinations of numerous and overlapping events for a week.
Usecase : 
* University Course Selection
* Workout Program
* Organised event management

### ARDate
* Dates defined as "ARDate" object.
* One date has one day, start and end hour.
* Date args : "mon", "12:30", "16:30"

### ARProgram
* Events defined as "ARProgram" object.
* Every ARProgram has ARDate list. One program can has one or more dates. 
* Program priority can be used for maximizing priority point or chose one program over another.

### ARCalendar
* "ARCalendar" can store the all possible programs.
* Load and Save the calendars as .csv files.
* Calendar object details are important for user.

### ARScheduler
* "ARScheduler" schedules every possible combination of programs. And tests it with requirements.

### calendar.csv
* csv formatting : <programname>,<priority>,<date1>,<date2>,<date3>...

### Usage :
1. Fill the example calendar

2. Select and edit example the function
```py
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
```

