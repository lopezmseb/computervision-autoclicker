#Created by Sebastian Lopez
#Imports
from tkinter import filedialog
import pyautogui as gui
import keyboard

class AutoClicker:
    #Class Variables
    START_TEXT = "Click on the AutoClicker you'd like to use:"

    def __init__(self):
        self.confidence = 0
        choice = gui.confirm(self.START_TEXT, title="AutoClicker", buttons=["Continuously Click", "Find Image Clicker"])
        #Choose Clicker
        if(choice == "Continuously Click"):
            self.continuous_clicker()
        elif(choice =="Find Image Clicker"):
            needle = filedialog.askopenfilename()
            self.get_confidence()
            self.find_clicker(needle)

    def find_image(self, needle):
        while(True):
            haystack = gui.screenshot()
            temp = gui.locate(needle,haystack,confidence = self.confidence)
            if(temp != None):
                return gui.center(temp)

    def continuous_clicker(self):
        gui.alert("Hold 'q' to pause and 'Esc' to quit!", title="AutoClicker")
        check = True
        while(check):
            gui.click()
            check = self.check_pause()

    def find_clicker(self, needle):
        gui.alert("Hold 'q' to pause and 'Esc' to quit!", title="AutoClicker")
        check=True
        while(check):
            location = self.find_image(needle)
            gui.click(location[0],location[1])
            check = self.check_pause()
            
    def check_pause(self):
        #Pause
        if(keyboard.is_pressed('q')):
            choice = gui.confirm(text="Paused!", title="AutoClicker: PAUSED", buttons=["Unpause", "Change Confidence"])
            if(choice == "Change Confidence"):
                self.get_confidence()
        #Exit Program
        elif(keyboard.is_pressed('Esc')):
            return False
        return True

    def get_confidence(self):
        check = True
        while(check):
            #Get New Confidence Level
            temp_conf = gui.prompt("Select Confidence Level (How Accurate the tracker is): (1-99)", title="AutoClicker: Set Confidence")
            #Try-Catch for invalid int parse
            try:
                temp_conf = int(temp_conf)
            except ValueError:
                #Change Value to int outside range
                gui.alert("Error: Number outside 1-99 or invalid input", title="AutoClicker: ERROR")
                continue
            #Catch Invalid Number Range
            if(temp_conf >= 1 and temp_conf < 100):
                self.confidence = float(temp_conf)/100
                check = False
            else:
                gui.alert("Error: Number outside 1-99 or invalid input", title="AutoClicker: ERROR")

AutoClicker()
