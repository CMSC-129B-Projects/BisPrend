import time
import threading
import threading
from balayQuizDatabase import *

from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.config import Config

#kivy uix
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

#kivymd
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField

from kivy.clock import Clock
from user import User

Config.set('graphics', 'resizable', True)

newPlayer = User() #global scope (for testing)

#Screens
class PageManager(ScreenManager):
    pass

class RegPage(Screen):
    
    def on_enter(self):
        Clock.schedule_once(self.skip)

    def registerUser(self):
        newPlayer.createUserFile(self.username.text)
        print(f"Name: {newPlayer.getName()} \nProgress: {newPlayer.getProgress()}")

    def skip(self,dt):
        if(not newPlayer.hasUser()):
            self.manager.current = 'Selector'
  
class BalayPage(Screen):
    pass

class BalayQuizPage(Screen):
    answerlist = []
    def appendAnswers(self, ans):
        self.answerlist.append(ans)
        self.checkanswer()
    def checkanswer(self):
        conn = create_or_open_db('BalayQuiz.db')
        cur = conn.cursor()
        correct_answer = extract_answer(cur)
        ind = self.answerlist.index(self.answerlist[-1])
        correct = correct_answer[ind]
        if self.answerlist[-1] == correct[0]:
            print(self.answerlist[-1] + " Correct")
        else:
            print(self.answerlist[-1] + " Incorrect")

    pass


class SkuylahanPage(Screen):
    pass

class MenuSelector(Screen):
    def playername(self):
        return newPlayer.getName()
    pass

class BisprendApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.primary_hue= "A700"
        self.theme_cls.accent_palette = "LightGreen"
        self.theme_cls.accent_hue = "A700"
        self.root = Builder.load_file("bisprend.kv")



#Registering Font
LabelBase.register(name="Mont",
    fn_regular= "Mont-ExtraLightDemo.otf", 
    fn_bold = "Mont-HeavyDEMO.otf"
)

if __name__ == '__main__':
    BisprendApp().run()