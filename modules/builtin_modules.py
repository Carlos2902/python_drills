#this is an example of a built-in module in python
#1. Import 
import sys
#save into a variable, and apply one of its methods
location = sys.path
#Print each route in the directory of sys
for n in location:
    print('\n',n)

#More examples of built-in modules
import calendar
leap_year = calendar.leapdays(2000,2024)

print(leap_year)
#Use of the isleap method of the 'calendar' module
is_leap_year = calendar.isleap(2024)
print(is_leap_year)