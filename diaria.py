#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.app import Widget
from datetime import date
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.core.window import Window;
from kivy.uix.bubble import Bubble, BubbleButton

hoje = date.today()
amanha = hoje.day
ontem = hoje.month
semana = hoje.weekday
dias = (0, 1, 2, 3, 4, 5, 6)
feira = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
i = 0

class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)
		
	def dia(self):
		global x
		x = dias[hoje.weekday()]
		if x == 0:
			App.get_running_app().root.current = 'seg'
		elif x == 1:
			App.get_running_app().root.current = 'ter'
		elif x == 2:
			App.get_running_app().root.current = 'qua'
		elif x == 3:
			App.get_running_app().root.current = 'qui'
		elif x == 4:
			App.get_running_app().root.current = 'sex'
		elif x == 5:
			App.get_running_app().root.current = 'sab'
		elif x == 6:
			App.get_running_app().root.current = 'dom'

class SegundaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'seg'
		super(Screen,self).__init__(**kwargs)

class TercaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'ter'
		super(Screen,self).__init__(**kwargs)

class QuartaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'qua'
		super(Screen,self).__init__(**kwargs)

class QuintaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'qui'
		super(Screen,self).__init__(**kwargs)

class SextaScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'sex'
		super(Screen,self).__init__(**kwargs)

class SabadoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'sab'
		super(Screen,self).__init__(**kwargs)

class DomingoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dom'
		super(Screen,self).__init__(**kwargs)

class RootScreen(ScreenManager):
    pass
    
class diariaApp(App):
	title = 'Labeeel!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = diariaApp()
    diariaApp().run()
