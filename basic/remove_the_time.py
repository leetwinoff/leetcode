"""
 You're re-designing a blog, and the blog's posts have the Weekday Month Day,
 time format for showing the date and time when a post was made, e.g., Friday May 2, 7pm.
 You're running out of screen real estate, and on some pages you want to display a shorter format,
 Weekday Month Day that omits the time.

 Write a function that takes the website date/time in its original string format and returns the shortened format.

 Input will always be a string, e.g., "Friday May 2, 7pm".
 Output will be the shortened string, e.g., "Friday May 2".
"""

def shorten_to_date(long_date: str) -> str:
    return long_date.split(",")[0]

print(shorten_to_date("Monday February 2, 8pm"))
print(shorten_to_date("Tuesday May 29, 8pm"))


def shorten_to_date2(long_date: str) -> str:
    return long_date[:long_date.index(",")]

print(shorten_to_date2("Monday February 2, 8pm"))
print(shorten_to_date2("Tuesday May 29, 8pm"))