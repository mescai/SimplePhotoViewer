
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
                print file
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

if __name__=="__main__":
    def reg():
        s1=en1.get()
        s2=en1.get()
        t1=len(s1)
        t2=len(s2)



    xin=Tk()
    la1=Label(xin,text="user").grid(row=0,sticky=W)
    la2=Label(xin,text="password").grid(row=1,sticky=W)
    la3=Label(xin).grid(row=3,sticky=W)

    en1=Entry(xin).grid(row=0,column=1,sticky=E)
    en2=Entry(xin).grid(row=1,column=1,sticky=E)
    en2["show"]="*"

    bu=Button(xin,text="sign in").grid(row=2,column=1,sticky=E)



    xin.mainloop()
