import kivy
import subprocess
from kivy.app import App
kivy.require('1.11.1')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.slider import Slider
from kivy.properties import ObjectProperty, ListProperty, StringProperty
import fileinput
import sys
import re
import os, signal

# Setting size to resizable
Config.set('graphics', 'resizable', 1)

# Creating a Layout class
class SettingsLayout(GridLayout):
    def parameters(self, data):
        with open("../build/genImgVertLines.ini", "r") as file:
            #read a list of lines into data
            data = file.readlines()
        data[3] = self.display1.text+'\n'
        data[4] = "#Image_height\n"
        data[5] = self.display2.text+'\n'
        data[6] = "#num_of_vertical_lines\n"
        data[7] = self.display3.text+'\n'
        with open("../build/genImgVertLines.ini", "w") as file:
            file.writelines( data )

class SettingsLayoutScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

# Creating App class
class GenimgvertlinesApp(App):
    with open("../build/genImgVertLines.ini", "r") as f:
        dat = f.readlines()
        disp1 = dat[3]
        disp2 = dat[5]
        disp3 = dat[7]
    def execute(self):
        s = subprocess.check_call("cd ../build/; ./genImgVertLines.bin", shell = True)
    def build(self):
        return ScreenManagement()

# Creating object and running it
genimgvertlinesApp = GenimgvertlinesApp()
genimgvertlinesApp.run()
