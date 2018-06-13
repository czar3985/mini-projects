# Mini-Projects Folder

**1. Break Timer**

This program can run on the background while a user is doing work on the computer. 
When it's time for the user to take a break, the program opens up a video on the 
web browser and plays a song as a signal to the user to pause his work.

Script: `break_time.py`

Notes: Customizable parts of the code are time between breaks, number of interruptions 
for the entire session and video that opens up to signal break time.

Current defaults:
```
timeBetweenBreaks = 3600 ## Time in seconds 
numCycles = 3 ## Number of interruptions 
url = "https://www.youtube.com/watch?v=XqZsoesa55w" ## Shark Dance video
```

**2. Turtle Drawings**

Uses Python's Turtle graphics library

`villager.py` draws a Minecraft villager head.
`flower.py` draws a flower

**3. Secret Message**

The secret message decoder takes a secret message from the files in the folder `decodeThis`.
Running the program will rename the files to remove the numbers from the file names. 
When the files are sorted, a secret message will appear.

Script: `rename_files.py`

Prerequisite: Python 2.7.5

Note: The translate method should be modified for Python 3.x.

**4. Send Text**

**5. Profanity Checker**