#python date-its a datatype in pyjton actually we nrrd to inport datime module to work with dates as date obejects
import datetime
x=datetime.datetime.now()
print(x) #2024-06-12 16:21:45.123456 current date and time

#The date contains year, month, day, hour, minute, second, and microsecond.
print(x.year) #2024
print(x.month) #9
print(x.minute) #4
print(x.day) #6

x = datetime.datetime(2020, 5, 17)

print(x) #2020-05-17 00:00:00
x = datetime.datetime.now()

print(x.strftime("%B")) #full month output-septembeer
print(x.strftime("%A")) #full day output-saturday
print(x.strftime("%a")) #short day output-sat
print(x.strftime("%b")) #short month output-sep
print(x.strftime("%Y")) #2025
print(x.strftime("%y")) #25
print(x.strftime("%d")) #06 day of month
print(x.strftime("%H")) #hour 24hr format 22
print(x.strftime("%I")) #hour 12hr format 10
print(x.strftime("%p")) #AM/PM PM
print(x.strftime("%M")) #minute 17
print(x.strftime("%S")) #second 45
print(x.strftime("%f")) #microsecond 123456 
print(x.strftime("%j")) #day of year 249
print(x.strftime("%U")) #week number of year from sunday 35
print(x.strftime("%W")) #week number of year form monday 36
print(x.strftime("%c")) #local date and time  Sat Sep  6 22:17:45 2025
print(x.strftime("%x")) #local date  09/06/25
print(x.strftime("%X")) #local time 22:17:45
print(x.strftime("%%")) #%  to print % sign



