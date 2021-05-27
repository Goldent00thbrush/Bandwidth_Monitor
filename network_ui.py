import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from network import network_stats

flag_first_run = True

def ref_data():# the actual content 
    ping_data.config(text=str(round(net_stats.ping_speed(),2))+" ms")
    download, upload = net_stats.download_upload_speed()
    if(download==-1 and upload==-1):
        messagebox.showerror("Error", "Cannot read wi-fi data")
        download = 0
        upload = 0
    download_data.config(text=str(round(download,2))+" KB/s")
    upload_data.config(text=str(round(upload,2))+" KB/s")
    time_now = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")
    time_tested.config( text="tested @ "+time_now)
    window.after(300000, ref_data)# refresh the data every 5 mins 

# styling parameters 
background = "white"
font_title = ("Bell MT",30 , "bold")
font_subtitles = ("Bell MT",20 , "bold")
color_title = "#fcc203"
color_subtitles = "#595854"
title_text = "Bandwidth Monitor"
padx_subtitle = (0, 40)
padx_text = (0, 40)
pady_subtitle = (25, 10)
pady_text = (5, 25)

#network obj
net_stats = network_stats()

#window creation
window = tk.Tk()
window.configure(background=background)
window.title(title_text)
# icon = tk.PhotoImage(file ='graph.png' )
# window.iconphoto(False, icon)
window.resizable(False, False)

#the main frames for the layouts
top_frame = tk.Frame(window)
center_frame= tk.Frame(window, background=background)
bottom_frame = tk.Frame(window)

label_title = tk.Label(master=top_frame, text=title_text, background=background, font=font_title, fg=color_title)
label_title.pack()

center_frame.grid_rowconfigure(1, weight=1)
center_frame.grid_columnconfigure(0, weight=1)

ping_title = tk.Label(master=center_frame, text="Ping", background=background,font= font_subtitles, fg=color_subtitles)
ping_title.grid(row=0, column=0,  padx=padx_subtitle,  pady=pady_subtitle)
ping_data = tk.Label(master=center_frame, background=background,font= font_subtitles, fg=color_subtitles)
ping_data.grid(row=1,column=0,  padx=padx_text,  pady=pady_text)

download_title = tk.Label(master=center_frame, text="Download", background=background,font= font_subtitles, fg=color_subtitles)
download_title.grid(row=0,column=1, padx=padx_subtitle,  pady=pady_subtitle)
download_data = tk.Label(master=center_frame, background=background,font= font_subtitles, fg=color_subtitles)
download_data.grid(row=1, column=1, padx=padx_text,  pady=pady_text)

upload_title = tk.Label(master=center_frame, text="Upload", background=background,font= font_subtitles, fg=color_subtitles)
upload_title.grid(row=0,column=2, padx=padx_subtitle,  pady=pady_subtitle)
upload_data = tk.Label(master=center_frame, background=background,font= font_subtitles, fg=color_subtitles)
upload_data.grid(row=1,column=2,padx=padx_text,  pady=pady_text)

time_tested = tk.Label(master=bottom_frame,background=background,font= font_subtitles, fg=color_subtitles)
time_tested.pack()

ref_data() 

# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="nw")
center_frame.grid(row=1, sticky="nw")
bottom_frame.grid(row=2, sticky="nw")

window.mainloop()