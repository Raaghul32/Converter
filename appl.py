# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 03:13:07 2020

@author: raagh
"""
import speech_recognition as SGR
from translate import Translator 
from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox as msg 
import os
import gtts as gt
import time
class Raaghul:
    def __init__(self, root):
        self.root = root 
        self.file_name = ''
        self.f = Frame(self.root,height=200,width=300)
        self.f.pack()
        self.message_label = Label(self.f,text="Raaghul's Converter",font = ('Arial', 19,'underline'),fg = 'Green')
        self.message_label2 = Label(self.f,text='Convert',font = ('Arial', 14,'underline'),fg = 'Red')
        self.convert_button = Button(self.f,text = 'Convert',font = ('Arial', 14),bg = 'Orange',fg = 'Black',command = self.converttts)
        self.speak_button = Button(self.f,text = 'Speak',font = ('Arial', 14),bg = 'Blue',fg = 'Black',command = self.convertstt)
        self.translate_button = Button(self.f,text = 'Translate',font = ('Arial', 14),bg = 'Purple',fg = 'Black',command = self.translate)
        self.exit_button = Button(self.f,text = 'Exit',font = ('Arial', 14),bg = 'Red',fg = 'Black',command = root.destroy)
        self.message_label.grid(row = 1, column = 1)
        self.message_label2.grid(row = 2, column = 1)
        self.convert_button.grid(row = 4, column = 0,padx = 0, pady = 15)
        self.speak_button.grid(row = 4, column = 1,padx = 10, pady = 15)
        self.translate_button.grid(row = 4, column = 2,padx = 10, pady = 15)
        self.exit_button.grid(row = 6, column = 1,padx = 10, pady = 15)
    def converttts(self):
        try:
            self.file_name = filedialog.askopenfilename(initialdir = '/Desktop',title = 'Select a Text file',filetypes = (('text file','*.txt'),('text file','*.txt')))
            fh = open(self.file_name,"r")
            mytext = fh.read().replace("\n","")
            myobj = gt.gTTS(mytext)
            myobj.save('op.mp3')
            os.system('start op.mp3') 
            msg.showinfo('Audio file created', 'Go to C users to find the audio file')
        except FileNotFoundError as e:
            msg.showerror('Error in opening file', e) 
    def convertstt(self):
        store=SGR.Recognizer()
        with SGR.Microphone() as s :
            msg.showinfo('Speak','Enable Microphone')
            audio_input = store.record(s,duration=10)
            msg.showinfo("Recording Time ",time.strftime("%M:%S"))
            try:
                text_output = store.recognize_google(audio_input)
                msg.showinfo('You spoke',text_output)
                msg.showinfo('Execution time',time.strftime("%M:%S"))
            except:
                msg.showerror('Error','oops,something is wrong.Try again')
    def translate(self):
        try:
            self.file_name = filedialog.askopenfilename(initialdir = '/Desktop',title = 'Select a Text file',filetypes = (('text file','*.txt'),('text file','*.txt')))
            fh = open(self.file_name,"r")
            mytext = fh.read().replace("\n","")
            translator = Translator(from_lang="English",to_lang= "German")
            op=translator.translate(mytext)
            text_file = open('converted.txt','wt')
            text_file.write(op)
            text_file.close()
            msg.showinfo('Converted','Check your directory')
            os.system('start converted.txt')
            
            
            
            
            
        except:
            msg.showerror('Error','oops,something is wrong')
            
            
        
        
            
                
        
root = Tk() 
root.title('Convert text to audio') 

obj = Raaghul(root) 
root.geometry('800x600') 
root.mainloop() 
        
        
        
        
        