# Code your functions here!

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.
def is_leap_year(year):
    return (year % 4 == 0)
    
print(is_leap_year(1990))
print(is_leap_year(1991))
print(is_leap_year(1992))   


# 2. Write a function that takes in the current year and returns a string telling when the next leap year will be.
def next_leap_year(year):
    remainder = year % 4
    time_to_next_ly = 4 - remainder
    next_ly = year + time_to_next_ly
    return next_ly

print next_leap_year(2001)        


# 3. Write a function that takes in two years as arguments (a start_year and a last_year), and then prints out every single year between them that is a leap year. 

print("Hello")
print("Hello Hello")