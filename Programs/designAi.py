from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def speakfun(event):
    pass
    # lis.config(text="Recognizing...")

# def releasefun(event):
#     lis.config(text="Released...")

root.title("Virtual Assistant")
root.wm_iconbitmap("micicon1.ico")


f1 = Frame(root,bg='#B5b1b1') #  #B5B1B1


image = Image.open('Mic.png')
image = image.resize((210,200),Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(image)



buttonmic = Button(f1,image=img1,bg='#B5b1b1',border='0',cursor='hand2')
buttonmic.place(x=220,y=50,width="250",height=230)
buttonmic.bind("<ButtonPress>", speakfun)
# buttonmic.bind("<ButtonRelease>", releasefun)


lis = Label(f1,text="Listening...",font="Century 18 normal",bg='#B5b1b1')
lis.place(x=260,y=300,width="200",height=40)

f1.place(x=0,y=0,width="700",height=430)



root.geometry("700x430")
# root.resizable(0,0)
root.mainloop()