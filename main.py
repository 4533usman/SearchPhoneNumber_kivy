# Program to Show how to use textinput
# (UX widget) in kivy using .kv file

# import kivy module	
import kivy
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
	
# base Class of your App inherits from the App class.	
# app:always refers to the instance of your application
from kivy.app import App
	
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Widgets are elements
# of a graphical user interface
# that form part of the User Experience.
from kivy.uix.widget import Widget

# The TextInput widget provides a
# box for editable plain text
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# The Label widget is for rendering text. 
from kivy.uix.label import Label
# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

# Create the widget class
class textinp(Widget):
	pass

# Create the app class
class MainApp(App):
	# Building text input
	def build(self):
		return textinp()  
	# Arranging that what you write will be shown to you
	# in IDLE
	#def process(self):
	#	text = self.root.ids.entry.text
	#	print(text)
	def checkrecord(self):
		text = self.root.ids.entry.text
		phoneNumber = phonenumbers.parse(text)
		print(phoneNumber)
		timeZone = timezone.time_zones_for_number(phoneNumber)
		Carrier = carrier.name_for_number(phoneNumber, 'en')
		Region = geocoder.description_for_number(phoneNumber, 'en')
		print(timeZone)
		print(Carrier)
		print(Region)
		
# Run the App

if __name__ == "__main__":
	MainApp().run()
