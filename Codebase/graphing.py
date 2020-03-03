import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk # Importing figure canvas for tkinter integration and also the navigation toolbar
from matplotlib.backend_bases import key_press_handler # Keypress handler
from matplotlib.figure import Figure # Figure is used for tkinter integration
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import numpy as np
from math import *
import gui
import cli
import sys

def Translate(timeInWords): # Needs string input of time in english words, standard grammar, no full stop.
    #timeInWords += " " # Add a space to allow for easy final word detection.
    words = [] # Storage for words.
    totalTime = 0 # Storage for total time conversion, in ns.
    timeConversion = {"SECONDS" : 1, "SECOND" : 1, "MINUTES" : 60, "MINUTE" : 60, "HOURS" : 3600,  "HOUR" : 3600, "DAY" : 86400, "DAYS" : 86400}
    # timeConversion is a dict used to translate the number & unit into seconds i.e. 3 Minutes is turned into 3 * 60 = 180 seconds.
    words = list(timeInWords.split(' '))

    while len(words) > 0: # As long as the list still has things in...
        timeUnit = words.pop()
        timeNumber = words.pop()
        totalTime += int(timeNumber) * timeConversion[timeUnit.upper()] # Add the transl;ated time to the total time.

    return totalTime

class dataGraph():
    def __init__(self):
        self._xList = []
        self._yList = []
        print("Data graph initialised.")

    def createBasicBarChart(self,f,barNames,barHeights): # If the barheights are already calculated.
        f.add_subplot(1,1,1)

        plt.bar(barNames,barHeights,align = 'center')

        return f

    def createStackedBarChart(self,f,timeGapPerReportedPosition,timePeriodPerBar,positionMeaning,positionList):
        indexDict = []
        if timePeriodPerBar > timeGapPerReportedPosition: # The time period per bar *must* be larger than the gap that the positions are reported in - else the program will break.
            # First job is to seperate positionList into meanings.
            tempList = []

            for meaning in positionMeaning: # For each meaning in the dict of meanings....
                itemChecker = positionMeaning[meaning] # Set the checker to the current meaning.
                for x in range(0, len(positionList)-1): # For each item in the position list
                    #print(x)
                    #print(positionList)
                    if positionList[x] == itemChecker: # Check if the current value is the one being searched for
                        tempList.append(1) # If it is, append 1 to the temporary list
                    else: # If it isn't...
                        tempList.append(0) # ... append 0.


                indexDict += [tempList] # Slowly creating a 2d list by storing each kind of action as a binary list of whether it's currently being performed.
                tempList = [] # Empty the temporary list once it's finished :)

            #print("INDEX")
            print(indexDict)
            barValues = []
            tempList = []

            print("Should be five:", round(timePeriodPerBar/timeGapPerReportedPosition))

            for listItem in indexDict: # For each list inside the index...
                loopInt = 1
                positionValue = 0
                for xy in listItem: # For each item inside each list...
                    if loopInt % round(timePeriodPerBar/timeGapPerReportedPosition) == 0:
                        #tempList.append(xy)
                        positionValue += xy
                        tempList.append(positionValue)
                        positionValue = 0
                    else:
                        positionValue += xy
                        #tempList.append(xy)

                    loopInt += 1

                barValues += [tempList]
                tempList = []

            print(barValues)









        else:
            print("The time period *must* be greater than the precision that the mouse is being tracked with!")
            '''
            popmessage = tk.Tk()
            popmessage.wm_title("Error")
            ttk.Label(popmessage, text = "The time period *must* be greater than the precision that the mouse is being tracked with!").pack()
            ttk.Button(popmessage, text = "Okay! :)", command = popmessage.destroy()).pack()
            popmessage.mainloop()
            '''

        return f




if __name__ == "__main__":
    jeff = Translate("4 days 3 Hours 23 Minutes 33 Seconds")
    print("Total Time in seconds: "+ str(jeff))

    newGraph = plt.Figure(facecolor="#202020")
    gen = dataGraph()

    xLabels = {"Sleeping":0,
    "Eating":1,
    "Moving":2,
    "Undefined":3}
    mouseReport = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2]

    newGraph = gen.createStackedBarChart(newGraph,1,5,xLabels,mouseReport)



    plt.show()
    input()
