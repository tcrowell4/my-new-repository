import datetime
import calendar

"""
challenge #15

Find the leap years beginning with a 1 and ending in a 6

he aint the youngest, he is the second
todo: buy flowers for tomorrow

Year 1176
Year 1356
Year 1576
Year 1756  <=== second  Mozart birthday
Year 1976

"""

# Python program to check if the input year is a leap year or not


def leap_year(year):
    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               #print("{0} is a leap year".format(year))
               return(True)
           else:
               pass
               #print("{0} is not a leap year".format(year))
       else:
           #print("{0} is a leap year".format(year))
           return(True)
    else:
       #print("{0} is not a leap year".format(year))
       pass

    return(False)

def is_jan26_dow_monday(year):
    date = datetime.date(year, 1, 26)
    return(date.weekday())


def main():
    for x in range(1006,1996,10):
        if calendar.isleap(x) == True:
            if is_jan26_dow_monday(x) == 0:
                print("Year %d" % x)

            

if __name__ == "__main__": 
    main()
