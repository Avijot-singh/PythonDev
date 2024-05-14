import time

timestamp = int(time.strftime('%H'))


if 5 <= timestamp < 12:
    print("Good morning")
elif 1 <= timestamp < 5:
    print("It is night time!")  
elif 18 <= timestamp < 22: 
    print("It is night time!")  
else:
    print("It is some other time!")
