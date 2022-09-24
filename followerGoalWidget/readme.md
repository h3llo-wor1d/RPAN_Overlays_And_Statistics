# "How Do I Use This Thing???"

## Part 1: Configuring Options.Temp.Json
- In order to use this, first, you need to edit options.temp.json to have your reddit username + pass in it.
> Follower data is not public for... whatever reason? so we need to spoof a logged in session!
- This data is not stored anywhere else! Take care in not accidentally showing this on-stream, please.
> Once you have finished changing the `username` and `password` parts of the file to your username and password, save it, 
> and rename it to options.json

## Part 2: Python
> This part is incredibly advanced, so if you don't know how to use Python or CMD, please do wait for the next release!
- This script uses the latest version of Python 3, but I reckon it will work with 3.8x as well.
- Install requirements.txt using PIP

## Part 3: Widget Customization
> This part requires minimal scripting knowledge!

In `overlay/` there is a file named `options.js`. This file contains all of the customization options for the widget.
Here is a list of what to edit/how to edit/if it should be edited:

### fontFile
Optionally, change this to the name of the font file you'd like to use. You need to have the file in the "overlay" folder.
The example, roobert.ttf has been provided. Please use the same syntax I have used for typing it, or it may not work!

### defaultBarColor
Optionally, this to the name of the color you would like to have the goal progress bar be.

### followerGoal
> You should absolutely edit this!

- Change this to the number of followers you'd like for the goal, there is no limit!

### followerGoalMessage
> You should absolutely edit this!

- Change this to the message you want on top of the widget!

> Do note, if it's too long, it will cut off

### backendPath
> You should absolutely NOT under basically ANY circumstances edit this

Only change this if you're also a software dev, and localhost:8000 is being used for another process for some reason.
Additionally, you need to change the port in `backend_PROTOTYPE.py`, obviously, as well, to match the port/stuff you use for this.
This is not recommended to be edited at all.


## Part 4: Adding into RPAN Studio/Activating
> This is the easiest part, assuming you got this far.

To add this to RPAN Studio, simply just drag overlay.html into it!

### In order to activate it, you NEED to start backend_PROTOTYPE.py
> It should start automatically, assuming you did everything right!

When I tested this on-stream, there was barely any latency at all for follower removals/additions.


## Part 5: Closing Stuff/FAQ

### When is the new version coming out?
- I am a student, but I will try my best to get it out there as soon as I can

### What about mac users?
- Is RPAN Studio even on Mac? Also, you just basically follow everything I said here, but the mac equivalent.

### How can I credit you?
- Absolutely feel free to just drop my name if someone asks how/where you got it, feel free to drop the repository as well!
- Additionally, feel free to leave a tip on my [ko-fi](https://ko-fi.com/h3llo_wor1d)! It helps me pay my bills, and helps pay for more future projects :)

### Are pull requests/feature requests for the project allowed?
- Absolutely!!! If you have any ideas for things you'd like to see, feel free to make a pull request, or throw a suggestion in the issues tab of the repository :)