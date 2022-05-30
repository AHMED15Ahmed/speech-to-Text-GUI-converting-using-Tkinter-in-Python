from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from gtts import gTTS
import speech_recognition as sr
import os

root= Tk()
root.title(' App-Speech-To-Text Converting ...')
root.geometry('500x500')
root.resizable(0, 0)
root.configure(bg='#FA5F05')
text1=''
file_name =("C:/Users/lenovo/Downloads/Tp1/python_test1/Rcording Voice python_project/APP_speech_to_text/record2.wav")
def recordvoice():
    while True:
        text1 =''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio)
                print(text1)
            except:
                pass
            return text1
def Filevoice():
    while True:
        text1 =''
        r = sr.Recognizer()
        with sr.AudioFile(file_name) as source: # open file 
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio)
                print(text1)
            except:
                pass
            return text1           
def Reset():
    txt_area.delete(1.0,END)            

 

#create icon
# Create a photoimage object of the image in the path
'''path3="C:/Users/lenovo/Downloads/Tp1/python_test1/Rcording Voice python_project/APP_speech_to_text/images/i5.png"
img1 = ImageTk.PhotoImage(Image.open(path3))
lebel_1=Label(root,bd=0,image=img1)
lebel_1.place(x=170,y=90)'''

button_icon1=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/Rcording Voice python_project/APP_speech_to_text/images/i5.png")
root.iconphoto(False,button_icon1)

button_icon2=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/Rcording Voice python_project/APP_speech_to_text/images/import.png")
root.iconphoto(False,button_icon2)

image_icon3=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/Rcording Voice python_project/APP_speech_to_text/images/res1.png")
root.iconphoto(False,image_icon3)
d_btn=Button(root,text='Reset',compound=LEFT,width=170,font='arial 20 bold ',image=image_icon3,relief=SUNKEN,bg='white',activebackground='Gold',bd=10,command=Reset)
d_btn.place(x=140,y=300)

txt_area = Text(root, font=('times new rommon',15,'bold'), height=3, width=25)
txt_area.place(x=120, y=200)
            
recordbutton = Button(root,compound=LEFT,width=100 ,font='arial 9 bold',text='Recording', bg='#9B755F',image=button_icon1,activebackground="gold", command=lambda: txt_area .insert(END, recordvoice()))
recordbutton.place(x=50, y=50)
filebutton = Button(root,compound=LEFT,width=100 ,font='arial 10 bold',text='IMport', bg='#9B755F',image=button_icon2,activebackground="gold", command=lambda: txt_area .insert(END, Filevoice()))
filebutton.place(x=300, y=50)
 
Label(root, text=' Speech-To-Text ',font="arial 20", bg='gold').place(x=110, y=0)
 
#Speech_to_text_button = Button(root, text='Speech-To-Text Conversion', font="arial 25", bg='#33A5FF', command=Speech_To_Text)
#Speech_to_text_button.place(x=50, y=250)
 
root.update()
root.mainloop()