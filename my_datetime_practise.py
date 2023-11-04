
import datetime,platform, random

# module_name.object.function
x = datetime.datetime.now()

d = datetime.date(2023, 7, 25)
# print(d)

# strftime: datetime to string

year = x.strftime("%Y")
# print("year:", year)

# creating Date Objects

x = datetime.datetime(2021,1,18)
# print(x)

# print(dir(datetime))
#
# x = platform.system()
# print(x)

"""
Directive	Description	                            Example	
%a	        Weekday, short version	                Wed	
%A	        Weekday, full version	                Wednesday	
%w	        Weekday as a number 0-6, 0 is Sunday	3	
%d	        Day of month 01-31	                    31	
%b	        Month name, short version	            Dec	
%B	        Month name, full version	            December	
%m	        Month as a number 01-12	                12	
%y	        Year, short version, without century	18	
%Y	        Year, full version	                    2018	
%H	        Hour 00-23	                            17	
%I	        Hour 00-12	                            05	
%p	        AM/PM	                                PM	
%M	        Minute 00-59	                        41	
%S	        Second 00-59	                        08	
%f	        Microsecond 000000-999999	            548513	
%z	        UTC offset	                            +0100	
%Z	        Timezone	                            CST
"""

list1 = [1,2,3,4,5,6]
# print(random.choice(list1))

print(random.seed(0))




















