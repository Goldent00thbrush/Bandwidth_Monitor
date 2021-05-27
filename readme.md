# A Bandwidth Monitor App
A simple wi-fi bandwidth monitor app built in Python.

## Introduction
The purpose of this project is to dive deeper into network interfaces and app building. The idea is building a simple real time bandwidth montior in form of a simple app like a small embedded device(which can only display it readings). It updates the UI every 5 mins.   
## The App

## Technologies 
-	Python 3.9.5
-   psutils
-	tkinter
-	pyinstaller
## Setup
-	Download and run the exe file in dist folder.
-	alternatively, could download the repo and run the network_ui.py file.(could run the following to pack into an exe:  pyinstaller --onefile  --hidden-import tkinter  --windowed network_ui.py) 
## Features/Components 
-	Simple UI
-	Network statistics class 
## Status 
The project is done. It took around 16 hours to develop (4 hours per week for 4 weeks).
## Future development
If the development of this project picks up again, here are things I want to work on or improve:
-	Interact with other network interfaces besides the wi-fi.
-   Handle different interface names.
-	A more friendly UI.
-	Pinging an optimial server (instead of Google's serevr). 
## Acknowledgments 
-	The idea was adopted from https://stackoverflow.com/questions/21866951/get-upload-download-kbps-speed  
-	The tutorial for creating the executable https://www.geeksforgeeks.org/convert-python-script-to-exe-file/ 
## License 
The source code for this project is licensed under the MIT license, which you can find in the MIT-LICENSE.txt file.
## Contact
Created by @goldent00thbrush - feel free to contact me!