from pytube import YouTube
import datetime

def start_download(tkinter_text_widget):
    try:
        video = YouTube(tkinter_text_widget.get())
        print(f"Vid Name: {video.title}, Length: {datetime.timedelta(seconds=video.length)}")
        stream = video.streams.get_highest_resolution()
        stream.download(output_path="videos")
        tkinter_text_widget.delete(0, len(tkinter_text_widget.get()))
    except Exception as error:
        print(error)