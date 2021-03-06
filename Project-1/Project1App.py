"""

Course Name: Embedded Interface Design
Author: Sridhar Pavithrapu
Project Description: Interfacing DHT22 Temperature/Humidity sensor with Raspberry Pi

"""

# Importing required modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import Adafruit_DHT

# Global variables section
sensor = 0
pin = 0
resolution = 0
temperatureList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
humidityList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""
Class to create GUI for two different resolutions (1013X584) and (800X480)
It also reads the Temperature and Humidity values from DHT22 sensor
Temperature and Humidity graphs are drawn by calling other calss function named-plot
"""
class Ui_Project1EID(object):

    # Initialization of GUI values
    def __init__(self):
        self.temperatureString = 0
        self.humidityString = 0
        self.temperatureCount = 0
        self.humidityCount = 0

    # Function to print temperature values along with error warning and printing time at which temperature is requested
    def temperatureReadingPrint(self):
        # Reading temperature and humidity values from DHT22 sensor
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Temperature:"+ str(self.temperatureString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        # Check for error condition
        if self.temperatureString is not None:
            self.temperature_Text.setText(str(self.temperatureString))
            self.temperature_Request_Time.setText(t.currentTime().toString())
            # Check for storing last 10 values
            if self.temperatureCount > 9:
                self.temperatureCount = 0
            
            temperatureList[self.temperatureCount] = self.temperatureString
            self.temperatureCount += 1
            print(temperatureList)
            # Check for alarm condition
            if self.temperatureString > 25 :
                self.Temperature_Alarm_GraphicsView.setStyleSheet("background: red")
            else:
               self.Temperature_Alarm_GraphicsView.setStyleSheet("background: green") 
                            
        else:
            self.temperature_Text.setText("Connection Failed")
            self.temperature_Request_Time.setText(t.currentTime().toString())
            
            
    # Function to print humidity values along with error warning and printing time at which humidity is requested        
    def humidityReadingPrint(self):
        # Reading temperature and humidity values from DHT22 sensor
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Humidity:"+ str(self.humidityString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        # Check for error condition
        if self.humidityString is not None:
            self.humidity_Text.setText(str(self.humidityString))
            self.humidity_Request_Time.setText(t.currentTime().toString())
            
            # Check for storing last 10 values
            if self.humidityCount > 9:
                self.humidityCount = 0
            
            humidityList[self.humidityCount] = self.humidityString
            self.humidityCount += 1
            print(humidityList)
            # Check for alarm condition
            if self.humidityString > 50 :
                self.humidity_Alarm_GraphicsView.setStyleSheet("background: red")
            else:
               self.humidity_Alarm_GraphicsView.setStyleSheet("background: green")
            
        else:
            self.humidity_Text.setText("Connection Failed")
            self.humidity_Request_Time.setText(t.currentTime().toString())
            
    # Function used for dynamic language translation	
    def retranslateUi(self, Project1EID):
        _translate = QtCore.QCoreApplication.translate
        Project1EID.setWindowTitle(_translate("Project1EID", "Project1EID"))
        self.temperature_Button.setText(_translate("Project1EID", "Temperature"))
        self.humidity_Button.setText(_translate("Project1EID", "Humidity"))
        self.temperature_Timeout_Label.setText(_translate("Project1EID", "Request Time"))
        self.humidity_Timeout_Label.setText(_translate("Project1EID", "Request Time"))
        self.temperature_Alarm_Label.setText(_translate("Project1EID", "TEMPERATURE ALARM"))
        self.humidity_Alarm_Label.setText(_translate("Project1EID", "HUMIDITY ALARM"))
        self.temperature_Graph_Button.setText(_translate("Project1EID", "Temperature_Graph"))
        self.humidity_Graph_Button.setText(_translate("Project1EID", "Humidity_Graph"))

    # Function for setting up UI
    def setupUi(self, Project1EID):
        Project1EID.setObjectName("Project1EID")
        # Check for different resolution
        if resolution == "1":
            print("In resolution (1013, 584)")
            Project1EID.resize(1013, 584)
            self.temperature_Button = QtWidgets.QPushButton(Project1EID)
            self.temperature_Button.setGeometry(QtCore.QRect(130, 120, 93, 28))
            self.temperature_Button.setObjectName("temperature_Button")
            self.humidity_Button = QtWidgets.QPushButton(Project1EID)
            self.humidity_Button.setGeometry(QtCore.QRect(140, 420, 93, 28))
            self.humidity_Button.setObjectName("humidity_Button")
            self.temperature_Text = QtWidgets.QLineEdit(Project1EID)
            self.temperature_Text.setGeometry(QtCore.QRect(250, 120, 161, 31))
            self.temperature_Text.setText("")
            self.temperature_Text.setObjectName("temperature_Text")
            self.humidity_Text = QtWidgets.QLineEdit(Project1EID)
            self.humidity_Text.setGeometry(QtCore.QRect(260, 420, 151, 31))
            self.humidity_Text.setObjectName("humidity_Text")
            self.temperature_Request_Time = QtWidgets.QLineEdit(Project1EID)
            self.temperature_Request_Time.setGeometry(QtCore.QRect(450, 120, 113, 31))
            self.temperature_Request_Time.setObjectName("temperature_Request_Time")
            self.humidity_Request_Time = QtWidgets.QLineEdit(Project1EID)
            self.humidity_Request_Time.setGeometry(QtCore.QRect(450, 420, 113, 31))
            self.humidity_Request_Time.setObjectName("humidity_Request_Time")
            self.temperature_Timeout_Label = QtWidgets.QLabel(Project1EID)
            self.temperature_Timeout_Label.setGeometry(QtCore.QRect(460, 100, 91, 20))
            self.temperature_Timeout_Label.setObjectName("temperature_Timeout_Label")
            self.humidity_Timeout_Label = QtWidgets.QLabel(Project1EID)
            self.humidity_Timeout_Label.setGeometry(QtCore.QRect(460, 400, 91, 20))
            self.humidity_Timeout_Label.setObjectName("humidity_Timeout_Label")
            self.Temperature_Alarm_GraphicsView= QtWidgets.QFrame(Project1EID)
            self.Temperature_Alarm_GraphicsView.setGeometry(QtCore.QRect(600, 90, 101, 101))
            self.Temperature_Alarm_GraphicsView.setStyleSheet("background: green")
            self.temperature_Alarm_Label = QtWidgets.QLabel(Project1EID)
            self.temperature_Alarm_Label.setGeometry(QtCore.QRect(590, 70, 131, 20))
            self.temperature_Alarm_Label.setObjectName("temperature_Alarm_Label")
            self.humidity_Alarm_Label = QtWidgets.QLabel(Project1EID)
            self.humidity_Alarm_Label.setGeometry(QtCore.QRect(610, 360, 101, 20))
            self.humidity_Alarm_Label.setObjectName("humidity_Alarm_Label")
            self.humidity_Alarm_GraphicsView= QtWidgets.QFrame(Project1EID)
            self.humidity_Alarm_GraphicsView.setGeometry(QtCore.QRect(610, 380, 101, 101))
            self.humidity_Alarm_GraphicsView.setStyleSheet("background: green")
            self.temperature_Graph_Button = QtWidgets.QPushButton(Project1EID)
            self.temperature_Graph_Button.setGeometry(QtCore.QRect(810, 130, 131, 28))
            self.temperature_Graph_Button.setObjectName("temperature_Graph_Button")
            self.humidity_Graph_Button = QtWidgets.QPushButton(Project1EID)
            self.humidity_Graph_Button.setGeometry(QtCore.QRect(810, 410, 131, 28))
            self.humidity_Graph_Button.setObjectName("humidity_Graph_Button")
        
        else :
                
            print("In resolution (800, 480)")
            Project1EID.resize(800, 480)
            self.temperature_Button = QtWidgets.QPushButton(Project1EID)
            self.temperature_Button.setGeometry(QtCore.QRect(20, 110, 93, 28))
            self.temperature_Button.setObjectName("temperature_Button")
            self.humidity_Button = QtWidgets.QPushButton(Project1EID)
            self.humidity_Button.setGeometry(QtCore.QRect(20, 350, 93, 28))
            self.humidity_Button.setObjectName("humidity_Button")
            self.temperature_Text = QtWidgets.QLineEdit(Project1EID)
            self.temperature_Text.setGeometry(QtCore.QRect(140, 110, 161, 31))
            self.temperature_Text.setText("")
            self.temperature_Text.setObjectName("temperature_Text")
            self.humidity_Text = QtWidgets.QLineEdit(Project1EID)
            self.humidity_Text.setGeometry(QtCore.QRect(140, 350, 151, 31))
            self.humidity_Text.setObjectName("humidity_Text")
            self.temperature_Request_Time = QtWidgets.QLineEdit(Project1EID)
            self.temperature_Request_Time.setGeometry(QtCore.QRect(340, 110, 113, 31))
            self.temperature_Request_Time.setObjectName("temperature_Request_Time")
            self.humidity_Request_Time = QtWidgets.QLineEdit(Project1EID)
            self.humidity_Request_Time.setGeometry(QtCore.QRect(330, 350, 113, 31))
            self.humidity_Request_Time.setObjectName("humidity_Request_Time")
            self.temperature_Timeout_Label = QtWidgets.QLabel(Project1EID)
            self.temperature_Timeout_Label.setGeometry(QtCore.QRect(350, 90, 91, 20))
            self.temperature_Timeout_Label.setObjectName("temperature_Timeout_Label")
            self.humidity_Timeout_Label = QtWidgets.QLabel(Project1EID)
            self.humidity_Timeout_Label.setGeometry(QtCore.QRect(340, 330, 91, 20))
            self.humidity_Timeout_Label.setObjectName("humidity_Timeout_Label")
            self.Temperature_Alarm_GraphicsView= QtWidgets.QFrame(Project1EID)
            self.Temperature_Alarm_GraphicsView.setGeometry(QtCore.QRect(490, 80, 101, 101))
            self.Temperature_Alarm_GraphicsView.setStyleSheet("background: green")
            self.temperature_Alarm_Label = QtWidgets.QLabel(Project1EID)
            self.temperature_Alarm_Label.setGeometry(QtCore.QRect(480, 60, 131, 20))
            self.temperature_Alarm_Label.setObjectName("temperature_Alarm_Label")
            self.humidity_Alarm_Label = QtWidgets.QLabel(Project1EID)
            self.humidity_Alarm_Label.setGeometry(QtCore.QRect(490, 290, 101, 20))
            self.humidity_Alarm_Label.setObjectName("humidity_Alarm_Label")
            self.humidity_Alarm_GraphicsView= QtWidgets.QFrame(Project1EID)
            self.humidity_Alarm_GraphicsView.setGeometry(QtCore.QRect(490, 310, 101, 101))
            self.humidity_Alarm_GraphicsView.setStyleSheet("background: green")
            self.temperature_Graph_Button = QtWidgets.QPushButton(Project1EID)
            self.temperature_Graph_Button.setGeometry(QtCore.QRect(620, 110, 131, 28))
            self.temperature_Graph_Button.setObjectName("temperature_Graph_Button")
            self.humidity_Graph_Button = QtWidgets.QPushButton(Project1EID)
            self.humidity_Graph_Button.setGeometry(QtCore.QRect(640, 340, 131, 28))
            self.humidity_Graph_Button.setObjectName("humidity_Graph_Button")
                
        # Intializing class objects for plotting temperature and humidity graphs
        self.main = TemperatureGraph()
        self.main_1 = HumidityGraph()

        # Function call backs for different button click
        self.retranslateUi(Project1EID)
        self.temperature_Graph_Button.clicked.connect(self.main.plot)
        self.humidity_Graph_Button.clicked.connect(self.main_1.plot)
        self.temperature_Button.clicked.connect(self.temperatureReadingPrint)
        self.humidity_Button.clicked.connect(self.humidityReadingPrint)
        QtCore.QMetaObject.connectSlotsByName(Project1EID)

"""
Class to create GUI for plotting temperature values
It plots the graph for latest ten temperature values
"""
class TemperatureGraph(QDialog):
    def __init__(self, parent=None):
        super(TemperatureGraph, self).__init__(parent)

        # Creating a figure instance to plot on
        self.figure = plt.figure()

        # Creating canvas widget that displays the `figure`
        self.canvas = FigureCanvas(self.figure)
        # Changing hthe window title as -Temperature graph
        self.setWindowTitle('Temperature Graph')
        
        # Creating a button and call back function call
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
       
        # Taking temperature values as input for plotting
        data = temperatureList

        # Create an axis
        ax = self.figure.add_subplot(111)

        # Clears the axes
        ax.clear()

        # Plot the data
        ax.plot(data, '*-')

        # Refresh canvas
        self.canvas.draw()
        self.show()

"""
Class to create GUI for plotting humidity values
It plots the graph for latest ten humidity values
"""
class HumidityGraph(QDialog):
    def __init__(self, title = 'Humidity Graph',parent=None):
        super(HumidityGraph, self).__init__(parent)

        # Creating a figure instance to plot on
        self.figure = plt.figure()

        # Creating canvas widget that displays the `figure`
        self.canvas = FigureCanvas(self.figure)
        # Changing hthe window title as -Humidity graph
        self.setWindowTitle('Humidity Graph')

        # Creating a button and call back function call
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        # Taking humidity values as input for plotting
        data = humidityList

        # Create an axis
        ax = self.figure.add_subplot(111)

        # Clears the axes
        ax.clear()

        # Plot the data
        ax.plot(data, '*-')

        # Refresh canvas
        self.canvas.draw()
        self.show()

# Main function definition
if __name__ == "__main__":
    import sys
	
    # Parse command line parameters.
    sensor_args = { '11': Adafruit_DHT.DHT11,
                    '22': Adafruit_DHT.DHT22,
                    '2302': Adafruit_DHT.AM2302 }
    # Check for input command line parameters
    if len(sys.argv) == 4 and sys.argv[1] in sensor_args:
       sensor = sensor_args[sys.argv[1]]
       pin = sys.argv[2]
       resolution = sys.argv[3]
    else:
       print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
       print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
       sys.exit(1)

    # Creating instance for the application and setting up the GUI 
    app = QtWidgets.QApplication(sys.argv)
    Project1EID = QtWidgets.QDialog()
    ui = Ui_Project1EID()
    ui.setupUi(Project1EID)
 
    # Show the GUI
    Project1EID.show()
    # Close the application
    sys.exit(app.exec_())
