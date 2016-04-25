
from Gui import *
from Tkinter import *
import Image as PIL
import ImageTk
import os

class SimpleImageBrower(Gui):
    """

    """


    def __init__(self):
        Gui.__init__(self)
        self.files=[]
        self.index=0


        self.button=self.bu(command=self.nextphoto,relief=FLAT)



    def nextphoto(self):
        try:
            if self.index<len(self.files):
                self.show_image(self.files[self.index])
                self.index+=1
                #print file
                self.mainloop()
            else:
                self.quit()
        except IOError as message:
            self.index+=1
            self.nextphoto()





    def image_loop(self,dirname="."):


        for file in os.listdir(dirname):
            self.files.append(dirname+file)
        self.show_image(self.files[self.index])

        self.index+=1
        self.mainloop()




    def show_image(self,filename):
        image=PIL.open(filename)
        self.photo=ImageTk.PhotoImage(image)
        self.button.config(image=self.photo)

from Tkinter import *

def test_label():
    def xinlabel(event):
        global xin
        s=Label(xin,text="I love python")
        s.pack(side="left",fill="both")

    xin=Tk()
    b1=Button(xin,text="creat label",background="red")
    b1.bind("<Button-1>",xinlabel)
    b1.pack()
    b1["width"]=30
    b1["background"]="green"

    xin.mainloop()

def create_user():
   xin=Tk()
   Label(xin,text="user:").grid(row=0,stick=W)
   Entry(xin).grid(row=0,column=1,sticky=E)

   Label(xin,text="password:").grid(row=1,sticky=W)
   Entry(xin).grid(row=1,column=1,stick=E)

   Button(xin,text="sign in").grid(row=2,column=1,sticky=E)
   xin.mainloop()

def simulate_button():
    xin=Tk()

    def xinlabel(event):
        global xin
        s=Label(xin,text="this is a label")
        s.pack()

    t=Label(xin,text="simulate button")
    t.bind("<Button-1>",xinlabel)
    t.pack()
    xin.mainloop()

def create_login():
    def reg():
        s1=en1.get()
        s2=en2.get()
        t1=len(s1)
        t2=len(s2)
        if s1=="111" and s2=="222":
            la3["text"]="login succeed"
        else:
            la3["text"]="user or password wrong"
            en1.delete(0,t1)
            en2.delete(0,t2)
    xin=Tk()
    la1=Label(xin,text="user")
    la1.grid(row=0,sticky=W)
    la2=Label(xin,text="password")
    la2.grid(row=1,sticky=W)
    la3=Label(xin)
    la3.grid(row=3,sticky=W)

    en1=Entry(xin)
    en1.grid(row=0,column=1,sticky=E)
    en2=Entry(xin,show="*")
    en2.grid(row=1,column=1,sticky=E)

    bu=Button(xin,text="sign in",command=reg)
    bu.grid(row=2,column=1,sticky=E)
    xin.mainloop()

def creat_menu():
    root=Tk()
    menubar=Menu(root)

    fmenubar=Menu(menubar)
    for item in ["new","open"]:
        fmenubar.add_checkbutton(label=item)

    fmenubar.add_separator()

    for item in ["save","save as"]:
        fmenubar.add_radiobutton(label=item)

    emenubar=Menu(master=menubar)
    for item in ["copy","past","cut"]:
        emenubar.add_command(label=item)

    vmenubar=Menu(menubar)
    for item in ["default view","novel view"]:
        vmenubar.add_command(label=item)

    amenubar=Menu(menubar)
    for item in ["version information","other message"]:
        amenubar.add_command(label=item)

    menubar.add_cascade(label="file",menu=fmenubar)
    menubar.add_cascade(label="edit",menu=emenubar)
    menubar.add_cascade(label="view",menu=vmenubar)
    menubar.add_cascade(label="about",menu=amenubar)

    root["menu"]=menubar

    root.mainloop()

def creat_popmenu():
    def xin():
        global root
        Label(root,text="I love python").pack()

    root=Tk()
    menubar=Menu(root)

    for x in ["vb","c","java","php"]:
        menubar.add_command(label=x)

    menubar.add_command(label="python",command=xin)

    def pop(event):
        menubar.post(event.x_root,event.y_root)

    root.bind("<Button-3>",pop)
    root.mainloop()





#this section should be interpreted by Python 3.X
from tkinter.dialog import *


