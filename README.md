# *AUTOPROGRAM*

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
* csv formatting : programname,priority,date1,date2,date3...