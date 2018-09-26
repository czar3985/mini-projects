# Mini-Projects Folder

**1. Break Timer**

This program can run on the background while a user is doing work on the computer. 
When it's time for the user to take a break, the program opens up a video on the 
web browser and plays a song as a signal to the user to pause his work.

Script: `break_time.py`

Notes: Customizable parts of the code are time between breaks, number of interruptions 
for the entire session and video that opens up to signal break time.

Current defaults:
```python
timeBetweenBreaks = 3600 ## Time in seconds 
numCycles = 3 ## Number of interruptions 
url = "https://www.youtube.com/watch?v=XqZsoesa55w" ## Shark Dance video
```

**2. Turtle Drawings**

Uses Python's Turtle graphics library

`villager.py` draws a Minecraft villager head.

`flower.py` draws a flower

**3. Secret Message**

The secret message decoder takes a secret message from the files in the folder _decodeThis_.
Running the program will rename the files to remove the numbers from the file names. 
When the files are sorted, a secret message will appear.

Script: `rename_files.py`

Prerequisite: Python 2.7.5

Note: The translate method should be modified for Python 3.x.

**4. Send Text**

The script sends a text message to a mobile phone via the Twilio service.

Script: `send_text.py`

Usage: 
- Install the Twilio Python package. Go to the command prompt 
and type `easy_install_twilio`
- Sign up for a Twilio account [here](https://www.twilio.com/try-twilio).
- From the Twilio console, take the Account SID, Auth token and twilio 
number
- The lines in the code to be modified: (Example doesn't show real values)
    ```python
    account_sid = "ACab1cde2345f6g78h9ij1k011121314m1"
    auth_token = "abc12defgh34i567j8k9101112m1314n"
    ```
    ```python
    body='Hello world',
    from_='+13123456789',
    to='+64123456789'
    ```

**5. Profanity Checker**

The program uses Google API in What Do You Like website for checking curse words.
Input is fed to this [site](http://www.wdylike.appspot.com/?q=) and it returns `true` 
or `false` depending on whether a curse word is detected.

Script: `profanity_checker.py`

Usage: Text input can be made through the console or through a file named 
_text_for_checking.txt_.
User is also asked whether line information where the curse word was detected
will be required. 

Sample output: Inappropriate word(s) found in line X: A line in a song lyrics with profanity here

To Do: Replace curse words when found with asterisks

**6. Geocode**

The program uses Google Maps' Geolocation api to convert an address into geographic
coordinates (latitude, longitude)

Script: `geocode.py`

Prerequisites: 
- Google developer account
- Google API key 
- A text file `google_api_key.txt` placed in the same folder as `geocode.py` containing 
the developer's Google API key
- python
- httplib2

Usage:
Import the method and pass the address string to the `getGeocodeLocation` method

Example:
```python
from geocode import getGeocodeLocation
getGeocodeLocation("Boracay, Philippines")
```