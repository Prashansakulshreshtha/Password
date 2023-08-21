from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabet=string.ascii_lowercase
    #print(small_alphabet)
    capital_alphabet = string.ascii_uppercase
    #print(capital_alphabet)
    numbers=string.digits
    specialchar=string.punctuation
    all=small_alphabet+capital_alphabet+numbers+specialchar
    password_length=int(length_box.get())
    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabet+capital_alphabet,password_length))
    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabet+capital_alphabet+numbers,password_length))
    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))
    #password=random.sample(all,password_length)
    #passwordfield.insert(0,password)
def copy():
    random_pass=passwordfield.get()
    pyperclip.copy(random_pass)
root=Tk()
root.config(bg='gray20')
choice=IntVar()
font=('arial',20,'bold')
passwordlabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordlabel.grid(pady=10)
weakradio=Radiobutton(root,text='Weak',value=1,variable=choice,font=font)
weakradio.grid(pady=5)
Mediumradio=Radiobutton(root,text='Medium',value=2,variable=choice,font=font)
Mediumradio.grid(pady=5)
strongradio=Radiobutton(root,text='Strong',value=3,variable=choice,font=font)
strongradio.grid(pady=5)
lengthlabel=Label(root,text='Password length',font=font,bg='gray20',fg='white')
lengthlabel.grid(pady=5)
length_box=Spinbox(root,from_=5,to_=20,width=5,font=font)
length_box.grid(pady=5)
generatebutton=Button(root,text='Generate',font=font,command=generator)
generatebutton.grid(pady=5)
passwordfield=Entry(root,width=20,bd=2,font=font)
passwordfield.grid(pady=5)
copybutton=Button(root,text='Copy',font=font,command=copy)
copybutton.grid(pady=5)
root.mainloop()