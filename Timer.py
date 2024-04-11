#import the time module
import time 

#input time in seconds
seconds=int(input("Enter the time in number of seconds"))

#function for timer
def countdowntimer(seconds):
 while seconds > 0:
    mins=int(seconds/60)
    secs=int(seconds%60)
    timer=f'{mins}:{secs}'
    print(timer,end="\r")
    time.sleep(1)
    seconds -=1
 print("Time Up")

#calling function
countdowntimer(seconds)