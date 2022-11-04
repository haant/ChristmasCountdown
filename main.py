import time
import datetime
import random

# Generate a random number
random1 = random.randint(1,3)

# ASCII file/image chooser 
if random1 == 1:
    f = open('tree.txt', 'r')
    content = f.read()
    picture = content
elif random1 == 2:
    f2 = open('santa.txt', 'r')
    content2 = f2.read()
    picture = content2
elif random1 == 3:
    f3 = open('snowman.txt', 'r')
    content3 = f3.read()
    picture = content3


def countdown(stop):
    print(picture) # Shows image
    while True:
        difference = stop - datetime.datetime.now() # Takes time now
        count_hours, rem = divmod(difference.seconds, 3600) # Difference in time now and time inputted 
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0: # Comapred when time is up
            print("Good bye!")
            break
        for x in range (1,2):
            # Displays countdown clock
            countdown = "Time left until Christmas: " + str(difference.days) + " Day(s) " + str(count_hours) + " Hour(s) " + str(count_minutes) + " Minute(s) " + str(count_seconds) + " Second(s) " * x
            print(countdown, end="\r") # Overwrites current line
            time.sleep(1)

end_time = datetime.datetime(2022, 12, 25, 00, 00, 0) # Date which is set

countdown(end_time)