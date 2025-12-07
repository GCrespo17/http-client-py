from tkinter import *
from tkinter import ttk
import client

window = Tk();
window.title("HTTP Client")
window.geometry("820x780");
#window.config(background = "#828282")

formFrame = Frame(window, relief = "groove")
formFrame.pack()


urlLabel = Label(formFrame, text = "URL: ").grid(row = 0, column = 0, padx = 5, pady = 5)

sendUrlEntry = Entry(formFrame)
sendUrlEntry.grid(row = 0, column = 1, padx = 5, pady = 5)
sendUrlEntry.config(width = 50)

def pressSendRequestBtn():
    urlContent = sendUrlEntry.get()
    client.sendHttpRequest(urlContent)


sendRequestBtn = Button(formFrame, text = "Enviar Solicitud")
sendRequestBtn.config(command = pressSendRequestBtn)
sendRequestBtn.config(activebackground = '#809096')
sendRequestBtn.grid(row = 0, column = 2, padx = 5, pady = 5)

# Iniciar la ventana
window.mainloop()

