import webbrowser
import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:
    def __init__(self):
        ## fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e210203cb15048148434bd2204cf780f').json()
        ## initial GUI Load
        self.load_gui()
        self.load_news_item(0)  # Calling instance method using self
        self.root.mainloop()

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='maroon')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        # clear the screen for next new news item
        self.clear()
        # placing the image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            self.photo = ImageTk.PhotoImage(im)
        except:

            img_url = "https://images.wondershare.com/repairit/aticle/2021/07/resolve-images-not-showing-problem-1.jpg"
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            self.photo = ImageTk.PhotoImage(im)


        label = Label(self.root, image=self.photo)
        label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'], background='maroon', foreground='white',
                        wraplength=350, justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], background='maroon',
                        foreground='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='maroon')
        frame.pack(expand=True, fill=BOTH)

        if index !=0:
            prev = Button(frame, text='Previous Article', width=16, height=3, background='white', foreground='maroon',
                      command=lambda:self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3, background='white', foreground='maroon',
                      command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index!=len(self.data['articles']) - 1:
            next = Button(frame, text='Next Article', width=16, height=3, background='white', foreground='maroon',
                      command=lambda:self.load_news_item(index+1) )
            next.pack(side=LEFT)

    def open_link(self, url):
        webbrowser.open(url)

        self.root.mainloop()
obj = NewsApp()