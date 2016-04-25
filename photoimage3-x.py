#this section should be interpreted by Python 3.X

from tkinter.dialog import *
from tkinter.messagebox import *

def create_dialog():

    def xin():
        d=Dialog(None,title="2014",text="satisfied?",bitmap=DIALOG_ICON,default=0,strings=("yes","so-so","no"))
        print (d.num)

    t=Button(master=None,text="survey",command=xin)
    t.pack()
    b=Button(master=None,text="quit",command=t.quit)
    b.pack()
    t.mainloop()



def creat_checkbutton():

    count1=0
    count2=0

    def xin1():
        nonlocal count1,la1
        if count1 % 2==0:
            count1+=1
            la1["text"]="2014 is selected"
        else:
            count1+=1
            la1["text"]="2014 is not selected"
    def xin2():
        nonlocal count2,la2
        if count2 % 2==0:
            count2+=1
            la2["text"]="2015 is selected"
        else:
            count2+=1
            la2["text"]="2015 is not selected"



    root=Tk()
    c1=Radiobutton(master=root,text="2014",command=xin1)
    c2=Radiobutton(master=root,text="2015",command=xin2)
    c1.pack()
    c2.pack()
    la1=Label(root,text="   ")
    la1.pack()
    la2=Label(root,text="   ")
    la2.pack()
    root.mainloop()

def creat_chess():
    root=Tk()
    can=Canvas(master=root,width=400,height=450)
    can.create_line((0,2),(400,2),width=2)
    for i in range(10):
        can.create_line((0,2+50*i),(400,2+50*i),width=2)
        can.create_line((i*50+2,2),(i*50+2,202),width=2)
        can.create_line((i*50+2,252),(i*50+2,450),width=2)
    can.create_line((150,0),(250,100),width=2)
    can.create_line((150,100),(250,0),width=2)
    can.create_line((150,450),(250,350),width=2)
    can.create_line((250,450),(150,350),width=2)
    can.create_text(20,220,text="chuhe")
    can.create_text(380,220,text="hanjie")

from tkinter.ttk import *

if __name__=="__main__":
    root=Tk()
    b=Button(root,text="xssss")
    b.pack()
    root.mainloop()
    