import os
import random
from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yars.settings')


import django
from django.db.models import Sum, Count
django.setup()
from tutti.models import User, Booking

numOfPeoplePerSlot = 30

def numSeatsForDate(date_string):
    # Return the number of seats left for a given date
    # Date is string with format yy-mm-dd
    dt = datetime.strptime(date_string, '%Y-%m-%d').date()
    nop = Booking.objects.filter(date=dt).aggregate(Sum('numberOfPeople'))
    if nop is None:
        nop = 0
    seats_left = numOfPeoplePerSlot - nop["numberOfPeople__sum"]
    return seats_left

def dateForNumSeats(numSeatRequested):
    # Return which date and time is available for that number of seats
    datetimeAvailable = {}
    results = (Booking.objects
               .filter(bookingStatus=True)
               .values('date', 'time')
               .annotate(dcount=Sum('numberOfPeople'))
               .order_by('date'))

    for result in results:
        if numOfPeoplePerSlot - result['dcount'] >= numSeatRequested:
            date = result['date']
            time = result['time']
            timeArr = datetimeAvailable.get(date, list())
            timeArr.append(time)
            datetimeAvailable[date] = timeArr

    return datetimeAvailable



if __name__ == "__main__":
    dateForNumSeats(10)