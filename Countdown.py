import time, pytz
from datetime import datetime
from zoneinfo import ZoneInfo

feature = input("What would you like to do? \nCountdown \nDisplay \n")

# Counting down section, enter a number then it loops to count down from there
if feature == "Countdown":
    time = int (input("Enter duration of countdown: "))

    while time > 0:
        time = time - 1
        print("Counting down from:", time)

        if time == 0:
            print("Time up!")

# Display section, taking in user's location and displaying their timezone info; atm it does just bases it on computer.... conversion update?
elif feature == "Display":
    while True:
        try:
            timezone = input("Enter timezone (Country/City):")
            py_timezone = pytz.timezone(timezone)
            current_datetime = datetime.now(py_timezone)
            print(current_datetime)
            break

        except pytz.UnknownTimeZoneError:
            print("Oops that timezone is not recognised! Please try again with timezone formats, here: "f"https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568")
    
        if timezone == "exit":
            break

   # local_time = time.localtime()
   # print("Your current timezone details are below: ")
   # print("Time Zone:", time.tzname)
   # print("Time Zone:", time.strftime("%Z", local_time))
   # print("Date and Time Zone:", time.strftime("%Y-%m-%d %H:%M:%S %Z", local_time) )
    # print("UTC Offset:", time.strftime("%z", local_time))

   # convert = input("Would you like to convert this to another timezone? (Y/N)")
    #    if convert =="Yes":
            
        
     #   else:
      #      print("Understandable, have a good day")


# country = input("What country are you from? \n")
   # city = input("What city in " + country + " are you located in? \n")
    #print("Alright, your date and timezone details for " + city + ", " + country + " are:")
#





