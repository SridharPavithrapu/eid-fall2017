# Embedded Interface Design
# Project-1
# Author: *Sridhar Pavithrapu*

**Project-1** description:
>Interfacing DHT22 Temperature/Humidity sensor with Raspberry Pi.
>This supports two different resolutions 1013X584(for Desktop) and 800X480(for Raspberry Pi touch screen LCD) for GUI.
>The GUI shows the temperature and humidity values on respective button is clicked, and also supports plotting temperature and humidity graphs.


**Installation Instructions:**
>First the Raspberry Pi is configured with Raspbian Stretch OS.
>RealVNC is installed and account is created to support remote development.
>Installed PyQT5 library in Raspberry Pi for developing GUI.
>DHT22 sensor is connected to respective GPIO pins. For reading values from the sensor, GPIO Pin #4 is used. 
>The below command is used to run the code:
'''
sudo python Project1App.py 22 4 1

Command Line Argument 1 - Sensor type
Command Line Argument 2 - GPIO pin used
Command Line Argument 3 - '1' for resolution (1013X584) else for resolution (800X480)

Eg-1: For desktop, 'sudo python Project1App.py 22 4 1'
      For touch screen, 'sudo python Project1App.py 22 4 2'
'''

**Project Work:**
>First the GUI is developed using QT designer.
>Then the .ui file is converted to .py file using the below command:
'''
> "C:\Python34\pyuic5.bat" -x Project1App.ui -o Project1App.py
'''
>Code is written to read temperature and humidity values from the sensor by installing the python libraries.
>Code also handles the error scenarios, and classes are written to plot temperature and humidity graphs for latest ten values in new windows.
>It also shows the alarm with red color image if temperature and humdity values exceeds the threshold.
>A temperature or button press shows its respective value along with the time when the request is made.


**Project Additions:**
>>Feature-1: Alarm indication when temperature and humidity values exceeds the threshold.
>>Feature-2: Support of two different resolutions for desktop and touch screen LCD.
>>Feature-3: Plotting temperature and humidity graphs for the latest ten values.

**Output:**
![alt-text-1](,"Resolution(800X480)") ![alt-text-2](,"Resolution(1013, 584)") 
![alt-text-1](,"Temperature Graph Demonstration") ![alt-text-2](,"Humidity Graph Demonstration")
![alt text](,"Alarm Demonstration") 

**References:**
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview
https://docs.python.org/3.4/
http://zetcode.com/gui/pyqt5/painting/
http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/




