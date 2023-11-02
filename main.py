import tkinter
import customtkinter

from download_youtube import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Download Youtube Video")

# UI Elements
title = customtkinter.CTkLabel(master=app, 
                               text="Paste Youtube Link", 
                               font=("FakeFont", 20))
title.pack(padx=10, pady=10, )

# Text Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download_button = customtkinter.CTkButton(app, 
                                          text="Download", 
                                          command=lambda: start_download(link), 
                                          font=("FakeFont", 16), 
                                          height=30)
download_button.pack(pady=20)


if __name__ == "__main__":
    app.mainloop()