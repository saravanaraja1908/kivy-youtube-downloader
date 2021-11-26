from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.button import MDRaisedButton,MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.config import Config
Config.set('graphics', 'resizable', True)
import webbrowser
from kivy.utils import get_color_from_hex
from pytube import YouTube
from pytube.cli import on_progress
from kivy.core.audio import SoundLoader

from os import path, makedirs
import certifi
import os
os.environ["KIVY_AUDIO"] = "ffpyplayer"

# Here's all the magic !
os.environ['SSL_CERT_FILE'] = certifi.where()
from kivy.clock import Clock
import ssl
import urllib.request as urlrq
import certifi
import ssl

resp = urlrq.urlopen('https://www.youtube.com/', context=ssl.create_default_context(cafile=certifi.where()))
import ssl
ssl.get_default_verify_paths()
from android.permissions import request_permissions, Permission,check_permission##
request_permissions([Permission.INTERNET,Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
helpstr = '''
ScreenManager:
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory
    
   
    Youtub:####YouTube downloader#####
########################################YOUTUBE VIDEO DOWNLOADER###########################################
<Youtub>:
    name:'youtub'
    FloatLayout:
        canvas.before:
            Color:
                rgba: rgba("#FFE4E1")
            Rectangle:
                size: self.size
                pos: self.pos
    Label:
        text: " YouTube Videos Downloader..."
        underline:True
        size_hint: [None, None]
        size: self.texture_size
        pos_hint: {"top":0.94, "center_x":0.5}
        font_size: "26sp"
        bold: True
        canvas.before:
            Color:
                rgba: rgba("#ff0000")
            Rectangle:
                size: self.size
                pos: self.pos
    MDTextFieldRect:
        id: url
        helper_text_mode: 'on_error'
        hint_text: "Only Paste YouTube Video url"
        background_color: [1,1,1,1]
        pos_hint: {'center_x':0.5,'center_y':0.8}
        color: [0,0,0,1]
        bold: True
        font_size: "20sp"
        multiline: False
        size_hint: [0.85, 0.06]  
    MDIconButton:
        icon: "youtube"
        user_font_size: "41dp" 
        pos_hint: {'center_x':0.4,'center_y':.86} 
        theme_text_color: "Custom"
        text_color: "#ff0000"  
        on_press: app.open1()
    MDLabel:
        text:'Goto youtube'
        pos_hint:{'center_x':.95,'center_y':.86}
        font_size: "15sp"
    
        
    MDLabel:
        text:'  click download!'
        pos_hint:{'center_x':0.8,'center_y':0.6}
        font_size: "20sp"
        color: "#ff0080" 
        underline:True
    MDIconButton:
        id:ss
        icon:'download'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#03ff00"
        user_font_size: '30sp'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: app.yturl()
    MDRoundFlatIconButton:    
        id:vid
        disabled: True
        bold:True
        icon: "video"
        text: "Download-Video"
        text_color:"#010000"
        line_color: "#05fa00"
        color: 1, 1, 1, 1
        font_size: "25sp"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        #size_hint: [0.3, 0.08]
        on_press:
            app.video_down(url.text)
    MDRoundFlatIconButton:
        id :aut
        disabled: True    
        line_color: "#ff0000"
        icon: "music"
        text_color:"#010000"
        text: "Download-Audio"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        #size_hint: [0.3, 0.08]
        font_size: "25sp"
        on_press:
            app.audio_down(url.text)        
    MDLabel:
        text:
            """*Paste youtube url then Choose the audio or video       and wait for Message.                 
            After completing your video or audio downloading...,
            .                     check your gallery or App file."""
        pos_hint: {'center_x':0.6,'center_y':0.2}
        bold:True
        font_size: "15sp"
    MDIconButton:
        icon: 'home'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#ff0000"
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '30sp'
        on_release:app.ext()
            
            


'''
class Youtub(Screen):#####YOUDUBE VIDEO DOWNLOADER#####
    pass
sm = ScreenManager()
sm.add_widget(Youtub(name='youtub'))######youtube video downloader####

class ytube(MDApp):######  main class   ######
    def build(self):
        self.strng = Builder.load_string(helpstr)

        return self.strng
    def keyboard(self,window,key,*args):
        print('dont presd'.str(key))
        if key == 27:
            self.transition.direction  = "right"
            self.current = "hello1"
    def ext(self):
        self.task1 = MDDialog(title='Are you sure?',type="confirmation",text=f"Are you sure you want to exit YouTube downloader app?",
                                buttons=[MDFlatButton(text="NO!",on_release=self.ta), MDRaisedButton(text="YES!",on_release=self.exte)])
        self.task1.open()

    def ta(self, obj):
        self.task1.dismiss()

    def exte(self, obj):
        self.stop()
    def yturl(self):
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='enter Youtube url?', text="Please enter Your Video url", size_hint=(0.7, 0.2),
                                   buttons=[check])
            self.check1.open()


        elif self.text.startswith('https://youtube.com/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtu.be/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.com/shorts/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.be/shorts/'):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.com/playlist?list='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://youtube.be/playlist?list='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False
        elif self.text.startswith('https://www.youtube.com/watch?v='):
            self.strng.get_screen('youtub').ids.aut.disabled = False
            self.strng.get_screen('youtub').ids.vid.disabled = False


        else:
            check2 = MDRaisedButton(text='Retry!', on_release=self.emdy)
            self.check02 = MDDialog(title='IN VALID URL! ', text="Please enter VALID URL!", size_hint=(0.7, 0.2),
                                   buttons=[check2])
            self.check02.open()

    def check01(self, obj):
        self.check1.dismiss()
    def emdy(self, obj):
        self.check02.dismiss()

    def video_down(self, url):
        sound1=SoundLoader.load('user.wav')
        if sound1:
            sound1.play()
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='Paste Youtub url?', text="Please enter YouTube Video url!",md_bg_color= get_color_from_hex('#FF3D00'), size_hint=(0.7, 0.2),radius=[20, 7, 20, 7],
                                   buttons=[check])
            self.check1.open()
        else:
            print('Please wait download video!')
            self.yt = YouTube(url)
            self.downloading_messag = MDDialog(title="Downloading...",
                                            text=f"Downloading.. {self.yt.title}")
            self.downloading_messag.open()


            # Checking if paths exists before downloading...
            file_path = "/storage/emulated/0/YouTube_downloader/Video"
            if not path.exists(file_path):
                makedirs(file_path, exist_ok=True)

            self.yt.streams.filter(progressive=True).get_highest_resolution().download(file_path)
            self.downloading_messag.dismiss()
            close_btn1 = MDRaisedButton(text="OK", on_press=self.close1_dialog)


            self.downloading_message = MDDialog(title="YouTube Video Download Completed...!",type="confirmation",md_bg_color= get_color_from_hex('#00FF00'),
                                            text=f"Successfully Downloaded![ {self.yt.title}]\n\nVideo Location ={file_path}",size_hint=(0.8, 0.3),radius=[20, 7, 20, 7],
                                            buttons=[close_btn1])
            self.downloading_message.open()
            print("successfully downloaded Video", file_path)
            sound2=SoundLoader.load('dearuser.wav')
            if sound2:
                sound2.play()
    def close1_dialog(self, obj):
        self.downloading_message.dismiss()



    def audio_down(self, url):
        sound3=SoundLoader.load('user.wav')
        if sound3:
            sound3.play()
        self.text = self.strng.get_screen('youtub').ids.url.text
        url_check_false = True

        try:
            int(self.text)
        except:
            url_check_false = False

        if url_check_false or self.text.split() == []:
        #if self.text.startswith==(""):
            check = MDRaisedButton(text='Retry!', on_release=self.check01)
            self.check1 = MDDialog(title='enter Youtub url?', text="Please enter Youtube Autio url!",md_bg_color= get_color_from_hex('#FF3D00'), size_hint=(0.7, 0.2),
                                   buttons=[check])
            self.check1.open()
        else:
            print('Please wait download autio!')
            yt = YouTube(url,on_progress_callback=on_progress)
            file_path1 = "/storage/emulated/0/YouTube_downloader/Audio"
            if not path.exists(file_path1):
                makedirs(file_path1, exist_ok=True)

            self.downloading_messag = MDDialog(title="Downloading...",
                                            text=f"Downloading.. {yt.title}")
            self.downloading_messag.open()

            audio_file = yt.streams.filter(only_audio=True).first().download(file_path1)
            base, ext =os.path.splitext(audio_file)
            new_file=base +".mp3"
            os.rename(audio_file,new_file)
            self.downloading_messag.dismiss()


            close_btn = MDRaisedButton(text="OK", on_press=self.close_dialog)

            self.downloading_message = MDDialog(title="Youtube Audio Download Completed...!",type="confirmation",md_bg_color= get_color_from_hex('#00FF00'),
                                            text=f"Successfully Downloaded!- [{yt.title}] \n\nAudio Location ={file_path1}",size_hint=(0.8, 0.3),
                                            buttons=[close_btn])
            self.downloading_message.open()
            print("Successfully Downloaded Audio",file_path1)
            sound4=SoundLoader.load('dearuser.wav')
            if sound4:
                sound4.play()
    def close_dialog(self, obj):
        self.downloading_message.dismiss()
    def open1(self):
        webbrowser.open("https://www.youtube.com/")
ytube().run()