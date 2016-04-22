
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

        self.button=self.bu(command=self.quit,relief=FLAT)

    def image_loop(self,dirname="."):

        files=os.listdir(dirname)

        for file in files:
            try:
                self.show_image(file)
                print file
                self.mainloop()
            except IOError:
                continue
            except:
                 break

    def show_image(self,filename):
        image=PIL.open(filename)
        self.photo=ImageTk.PhotoImage(image)
        self.button.config(image=self.photo)


if __name__=="__main__":
    g=SimpleImageBrower()
    g.image_loop("c:/test/")

