from tkinter import *
import pyperclip
import pyshorteners

def url_shortner():
    shortener = pyshorteners.Shortener()
    url_short = shortener.tinyurl.short(main_url.get())
    short_url.set(url_short)

if __name__=="__main__":
    root = Tk()
    root.geometry("700x700")
    root.title("URL Shortener")
    root.configure(bg="#a3c9cf")
    main_url = StringVar()
    short_url= StringVar()
    Label(root, text="Enter URL", font="Times").pack(pady=5)
    Entry(root,textvariable=main_url, width =70).pack(pady=5)
    Button(root, text="Generate Short URL", command =url_shortner).pack(pady=5)
    Entry(root, textvariable= short_url, width=70).pack(pady=4)
    root.mainloop()
