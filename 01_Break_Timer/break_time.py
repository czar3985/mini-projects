# MINI PROJECT: Break Timer
# DESCRIPTION: This program can run on the background while
# a user is doing work on the computer. When it's time for the user
# to take a break, the program opens up a video on the web browser
# and plays a song as a signal to the user to pause his work.

import webbrowser
import time

# Initializations
timeBetweenBreaks = 3600 ## Time in seconds 
numCycles = 3 ## Number of interruptions 
url = "https://www.youtube.com/watch?v=XqZsoesa55w" ## Shark Dance video
count = 1

print("Start time: " + time.ctime())

while (count <= numCycles):
    time.sleep(timeBetweenBreaks)

    # opens the Shark Dance video
    webbrowser.open(url)
    print("Break time: " + time.ctime())
    count = count + 1
    
print("End time: " + time.ctime())
