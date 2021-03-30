from tkinter import *
from pytube import *
from tkinter import ttk

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title(" Online Youtube Video Downloader")


Label(root,text = 'Online Youtube Video Downloader', font ='arial 20 ',foreground="#808080",bg='black').pack(side=TOP,fill=X)




##enter link
link = StringVar()

Label(root, text = 'Enter the URL:', font = 'arial 15').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link,bg='lightyellow').place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    url.streams.filter(adaptive=True).first().download(output_path="D:\\")
    Label(root, text = 'DOWNLOAD SUCCESSFUL...!', font = 'arial 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD ', font = 'arial 15 bold' ,bg = 'blue',fg='white', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()
