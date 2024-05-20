'''Issue #286 - Multiple METHOD: definitions in the calendar
->ValueError: A VCALENDAR must have at most one METHOD

   https://github.com/collective/icalendar/issues/286
'''
import os
from icalendar import Calendar

def test_issue_286():
    path = 'calendars/issue_286_multiple_methods.ics'
    print(path)
    with open(path) as f:
      calendar = Calendar.from_ical(f.read())
    print(calendar)
    print(Calendar(calendar))

test_issue_286()