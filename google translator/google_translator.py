from tkinter import *
import tkinter as  tk
from tkinter import ttk
from PIL import ImageTk, Image 
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('530x330')
root.maxsize(530,330)
root.minsize(530,330)


def translate():
    language_l = t1.get("1.0","end-1c")
    cl = choose_language.get()
    
    if language_l == '':
        messagebox.showerror('Language Translator','Please fill the box')
    else:
        translator = Translator()
        output = translator.translate(language_l, dest=cl)
        t2.insert('end',output.text)
        
def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')
    
    
img = ImageTk.PhotoImage(Image.open('translator1.png'))
label = Label(image=img)
label.place(x=(530 - 100) // 2,y=3)


a = tk.StringVar()
auto_detect = ttk.Combobox(root, width = 20, textvariable = a, state='readonly',font=('verdana',10,'bold'),)



auto_detect['values'] = (
                           'Auto Detect',
                           )
auto_detect.place(x=30, y=70)
auto_detect.current(0)



l = tk.StringVar()
choose_language = ttk.Combobox(root, width = 20, textvariable = l, state='readonly',font=('verdana',10,'bold'),)

choose_language['values'] = (
                               'Afrikaans',
                               'Arabic',
                               'Albanian',
                               ' Amharic',
                                'Akan',
                                'Bengali',
                                'Bulgarian',
                                'Basque',
                                'Belarusian',
                                'Chinese',
                                'Catalan',
                                'Cebuano',
                                'Croatian',
                                'Dutch',
                                'Danish',
                                'Dari',
                                'English',
                                'Esperanto',
                                'Estonian',
                                'French',
                                'Finnish',
                                'Filipino',
                                'German',
                                'Greek',
                                'Gujarati',
                                'Georgian',
                                'Hindi',
                                'Hungarian',
                                'Hebrew',
                                'Italian',
 
                                      )

choose_language.place(x=290,y=70)
choose_language.current(0)


t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)

t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)

button = Button(root, text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=200)

clear = Button(root, text="clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear)
button.place(x=280,y=200)
root.mainloop()

