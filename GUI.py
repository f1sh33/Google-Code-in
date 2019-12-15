import tkinter as tk
import requests

class Application(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.label = tk.Label(text="Codeforces Handle Info")
        self.pack()

        self.entry = tk.Entry()
        self.entry.pack()

        self.input = tk.StringVar()
        self.entry['textvariable'] = self.input

        self.checkBut = tk.Button(self)
        self.checkBut['text'] = 'Get Info'
        self.checkBut['command'] = self.process
        self.checkBut.pack()

    def process(self, event=None):
        userName = self.input.get()
        url = "https://codeforces.com/api/user.info?handles="
        url += userName
        result = requests.get(url)
        status = result.status_code
        result = result.json()

        if status != 200:
            label0 = tk.Label(self, text = "This username doesn't exist.")
            label0.pack()
        else:
            cRank = result["result"][0]["rank"]
            mRank = result["result"][0]["maxRank"]
            cRating = result["result"][0]["rating"]
            mRating = result["result"][0]["maxRating"]
            name = "Handle: " + userName
            cRank = "Current Rank: " + cRank
            mRank = "Max Rank: " + mRank
            cRating = "Current Rating: " + str(cRating)
            mRating = "Max rating: " + str(mRating)
        label5 =  tk.Label(self, text = name)
        label1 =  tk.Label(self, text = cRank)
        label2 =  tk.Label(self, text = mRank)
        label3 =  tk.Label(self, text = cRating)
        label4 =  tk.Label(self, text = mRating)
        label5.pack()
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()

root = tk.Tk()
app = Application(master=root)
app.master.title('My checker app')
app.master.minsize(300, 200)
app.mainloop()
