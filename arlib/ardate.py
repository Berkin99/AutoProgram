#  Author	: BerkN
#  Date		: 20.09.2024 14:34

__author__ = 'BerkN'
__all__ = ['ARDate','ARClass']

AR_DAYS = ("mon","tue","wed","thu","fri","sat","sun")

def timeToMins(tstr: str) -> int:
	hours, mins = map(int, tstr.split(":"))
	return hours * 60 + mins

def minsToTime(mins: int) -> str:
    hours = int(mins / 60) % 24
    mins = mins % 60
    return "{:02d}:{:02d}".format(hours, mins)

def dayToMins(tstr: str) -> int:
	return AR_DAYS.index(tstr) * 24 * 60

def minsToDay(mins: int) -> str:
	days = int(mins / (24 * 60))
	return AR_DAYS[days]

class ARClass:
	MON = (0x01<<0)
	TUE = (0x01<<1)
	WED = (0x01<<2)
	THU = (0x01<<3)
	FRI = (0x01<<4)
	SAT = (0x01<<5)
	SUN = (0x01<<6)
	
	def binaryDay(bin: int):
		ls = []
		for i in range(len(AR_DAYS)):
			if bin & (0x01 << i): ls.append(AR_DAYS[i])
		return ls

class ARDate:	
	"""	
		Istart and Iend as raw minutes of the week
		* day   : str "Mon"
		* start : str "HH:MM"
		* end   : str "HH:MM" 
	"""
	def __init__(self, day: str, start: str, end: str) -> None:
		day = day.lower()
		try: self.Iday   = AR_DAYS.index(day)
		except ValueError: print("ARDate> \"" + day + "\" is not a day.")
		
		self.Istart = dayToMins(day) + timeToMins(start)
		self.Iend   = dayToMins(day) + timeToMins(end)
		if not self.isValid(): 
			print("ARDate> date is not valid.")
			raise ValueError
	
	def getString(self) -> str:
		return AR_DAYS[self.Iday] + " " + minsToTime(self.Istart) + " " + minsToTime(self.Iend)
	
	def getDuration(self) -> int: # Duration as minutes
		return self.Iend - self.Istart

	def isValid(self) -> bool:
		return self.Istart < self.Iend
	
	def contains(self, rawmins: int) -> bool:
		if rawmins > self.Istart and rawmins < self.Iend: return True
		return False
	
	def __lt__(self, other: object) -> bool: return self.Iend <= other.Istart
	def __gt__(self, other: object) -> bool: return self.Istart >= other.Iend
	def __eq__(self, other: object) -> bool:
		if type(other) != type(self): return False 
		return not (self < other or self > other)
