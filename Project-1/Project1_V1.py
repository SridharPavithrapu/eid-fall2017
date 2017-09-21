# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1GUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

import Adafruit_DHT


sensor = 0
pin = 0


temperatureList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
humidityList = [None]*10	

class Ui_Project1EID(object):

    def __init__(self):
        self.temperatureString = 0
        self.humidityString = 0
        self.temperatureCount = 0
        self.humidityCount = 0

    def temperatureReadingPrint(self):
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Temperature:"+ str(self.temperatureString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        if self.temperatureString is not None:
            self.temperature_Text.setText(str(self.temperatureString))
            self.temperature_Request_Time.setText(t.currentTime().toString())
            if self.temperatureCount > 9:
                self.temperatureCount = 0
            
            temperatureList[self.temperatureCount] = self.temperatureString
            self.temperatureCount += 1
            print(temperatureList)
            if self.temperatureString > 25 :
                self.Temperature_Alarm_GraphicsView.setStyleSheet("background: red")
            else:
               self.Temperature_Alarm_GraphicsView.setStyleSheet("background: green") 
                    
                
        else:
            self.temperature_Text.setText("Connection Failed")
            
            
    def humidityReadingPrint(self):
        self.humidityString, self.temperatureString = Adafruit_DHT.read_retry(sensor, pin)
        t = QtCore.QTime()
        print("Humidity:"+ str(self.humidityString) + " at Time:"+ t.currentTime().toString())
        print("\n")
        if self.humidityString is not None:
            self.humidity_Text.setText(str(self.humidityString))
            self.humidity_Request_Time.setText(t.currentTime().toString())
            
            if self.humidityCount > 9:
                self.humidityCount = 0
            
            humidityList[self.humidityCount] = self.humidityString
            self.humidityCount += 1
            print(humidityList)
            if self.humidityString > 50 :
                self.humidity_Alarm_GraphicsView.setStyleSheet("background: red")
            else:
               self.humidity_Alarm_GraphicsView.setStyleSheet("background: green")
            
        else:
            self.humidity_Text.setText("Connection Failed")
            
	
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

    def setupUi(self, Project1EID):
        Project1EID.setObjectName("Project1EID")
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
        self.main = TemperatureGraph()
        self.main_1 = HumidityGraph()

        self.retranslateUi(Project1EID)
        self.temperature_Graph_Button.released.connect(self.main.plot)
        self.humidity_Graph_Button.released.connect(self.main_1.plot)
        self.temperature_Button.released.connect(self.temperatureReadingPrint)
        self.humidity_Button.released.connect(self.humidityReadingPrint)
        QtCore.QMetaObject.connectSlotsByName(Project1EID)

class TemperatureGraph(QDialog):
    def __init__(self, parent=None):
        super(TemperatureGraph, self).__init__(parent)
        
        # self.templist  = [None]*10

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = temperatureList

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()
        self.show()


class HumidityGraph(QDialog):
    def __init__(self, parent=None):
        super(HumidityGraph, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = humidityList

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()
        self.show()


if __name__ == "__main__":
    import sys
	
    # Parse command line parameters.
    sensor_args = { '11': Adafruit_DHT.DHT11,
                    '22': Adafruit_DHT.DHT22,
                    '2302': Adafruit_DHT.AM2302 }
    if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
       sensor = sensor_args[sys.argv[1]]
       pin = sys.argv[2]
    else:
       print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
       print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
       sys.exit(1)
	
    app = QtWidgets.QApplication(sys.argv)
    Project1EID = QtWidgets.QDialog()
    ui = Ui_Project1EID()
    ui.setupUi(Project1EID)
 
    
    Project1EID.show()
    sys.exit(app.exec_())

