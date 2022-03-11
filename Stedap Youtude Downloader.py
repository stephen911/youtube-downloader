# Importing all the necessary modules for Python YouTube Video Downloader project
from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube
from easygui import diropenbox
from pyautogui import hotkey

# Defining the downloader function for YouTube Video Downloader project using Python
def downloader(link, directory, filename):
    yt_link = link.get()
    save_path = directory.get()
    aftersave_filename = filename.get()

    try:
        yt = YouTube(yt_link)
        video = yt.streams.first()
        video.download(save_path, aftersave_filename)
    except Exception as e:
        mb.showerror('Error', f'Connection Error! You are offline! {e}')


def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set('')
    d_strvar.set('')
    fn_strvar.set('')


def browse():
    path = diropenbox()
    if path is None:
        pass
    else:
        dir_entry.insert(END, path)


def paste():
    hotkey("ctrl", "v")








# Initializing the window
root = Tk()
root.title('Stedap Youtube Video Downloader')
root.geometry('600x250')
root.resizable(0, 0)
root.config(bg='red')

# Heading label
Label(root, text='Stedap Youtube Video Downloader', fg="white", font=("Comic Sans MS", 15), bg='red').place(relx=0.25, rely=0.0)

# Creating the main window
Label(root, text='Download link:', fg="white", font=("Times New Roman", 13), bg='red').place(relx=0.05, rely=0.2)

link_strvar = StringVar(root)
link_entry = Entry(root, width=50, textvariable=link_strvar)
link_entry.place(relx=0.25, rely=0.2)
link_entry.focus()
paste_btn = Button(root, text='Paste', font=4, bg='Aquamarine',
                      command=lambda: paste()).place(relx=0.8, rely=0.15)

browse_btn = Button(root, text='Browse', font=4, bg='Aquamarine', height=1,
                      command=lambda: browse()).place(relx=0.8, rely=0.34)

Label(root, text='Save To:', fg="white", font=("Times New Roman", 13), bg='red').place(relx=0.05, rely=0.4)

dir_strvar = StringVar(root)
dir_entry = Entry(root, width=50, textvariable=dir_strvar)
dir_entry.place(relx=0.3-0.05, rely=0.4)


Label(root, text='filename:', fg="white", font=("Times New Roman", 13), bg='red').place(relx=0.05, rely=0.6)

filename_strvar = StringVar(root)
filename_entry = Entry(root, width=50, textvariable=filename_strvar)
filename_entry.place(relx=0.3-0.05, rely=0.6)

# Creating the buttons
download_btn = Button(root, text='Download', font=7, bg='Aquamarine',
                      command=lambda: downloader(link_entry, dir_entry, filename_entry)).place(relx=0.3-0.05, rely=0.75)

reset_btn = Button(root, text='Reset', font=7, bg='Aquamarine',
                   command=lambda: reset(link_strvar, dir_strvar, filename_strvar)).place(relx=0.5-0.05, rely=0.75)

# Finalizing the window of Python YouTube Video Downloader project
root.update()
root.mainloop()