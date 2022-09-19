import tkinter as tk
from turtle import right
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import *

window = tk.Tk()
def widgets():
    window.title("Youtube downloder")
    window.minsize(350,150)
    window.configure(bg="black")
    frame_1 = tk.Frame(window).pack()
    frame_2 = tk.Frame(window).pack()

    lable_1 = tk.Label(frame_1,text="Vidio link",bg="black",fg="red",width=40,height=2).pack()
    entry_1 = tk.Entry(frame_1,bg="gray",fg="red",width=40,textvariable=vidio_link).pack()


    lable_2 = tk.Label(frame_1,text="Directory",bg="black",fg="red",width=40,height=2).pack()
    entry_2 = tk.Entry(frame_1,bg="gray",fg="red",width=40,textvariable=downlod_dir).pack(pady=20)

    button_1 = tk.Button(text="Open file",bg="gray",fg="red",width=40,height=1,command=brows).pack()
    button_2 = tk.Button(text="Downlod now",bg="gray",fg="red",width=40,height=1,command=downlod).pack()
    button_3 = tk.Button(text="exit",bg="gray",fg="red",width=40,height=1,command=exit).pack()


def brows():

    directory = askdirectory(initialdir="YOUR DIRECTORY PATH",title="save")
    print(directory)
    downlod_dir.set(directory)
def downlod():
    link = vidio_link.get()
    save_vidio = downlod_dir.get()
    yt = YouTube(link)
    yt.streams.first().download(save_vidio)
    messagebox.showinfo(title="Sucsess",message="download done !")
downlod_dir = tk.StringVar()
vidio_link = tk.StringVar()


widgets()
if __name__ == "__main__":
    window.mainloop()
