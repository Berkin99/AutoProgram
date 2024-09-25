#  Author	: BerkN
#  Date		: 20.09.2024 14:34

from arlib.ardate import *
from arlib.arprogram import ARProgram
from arlib.arcalendar import ARCalendar

""" Format : 'mon 10:30 12:30' """
def createDate():
	while 1:
		s = input("Date: ")
		if len(s) == 0: return None
		arg = s.split()
		try: return ARDate(arg[0], arg[1], arg[2])
		except ValueError: continue
		except IndexError: continue
		
""" Format : 'MATH101, 3, mon 10:30 12:30, sat 13:30 16:00' """
def createProgram():
	name = input("Program name: ").strip()
	if len(name) == 0: return None
	pri  = input("Priority: ").strip()
	prog = ARProgram(name, int(pri))
	date = None
	while 1:
		date = createDate()
		if date == None: break
		prog.append(date)
	return prog

def createCalendar():
	print("ARClient> Creating Calendar")
	calendar = ARCalendar()
	i = 0
	while 1:
		print("Program [{:d}]".format(i))
		prog = createProgram()
		if prog == None: break
		calendar.append(prog, force=True)
		i += 1
	return calendar
