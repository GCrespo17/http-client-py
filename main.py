from tkinter import *
from tkinter import ttk
import client

response = None


#Formatear mi encabezado para que los ojos no sufran
def formatHeaders(headers, status, reason, version):
    httpVersion = f"HTTP/{version // 10}.{version % 10}"
    formattedText = f"{httpVersion} {status} {reason}\n\n"
    for key, value in headers:
        formattedText += f"{key}: {value}\n\n"
    return formattedText

#Imprime la informacion dada
def printHeaderTextInfo(header):
    headerText.config(state = NORMAL)
    headerText.delete("1.0", END)
    headerText.insert("1.0", header)
    headerText.config(state = DISABLED)

def printBodyTextInfo(body):
    bodyText.config(state = NORMAL)
    bodyText.delete("1.0", END)
    bodyText.insert("1.0", body)
    bodyText.config(state = DISABLED)

#Funcion que se activa cuando se presiona el boton de enviar solicitud
def pressSendRequestBtn():
    urlContent = sendUrlEntry.get()
    if (option.get() == "GET"):
        response = client.sendRequest(urlContent, option.get())
    elif (option.get() == "HEAD"):
        response = client.sendRequest(urlContent, option.get())
    headers = formatHeaders(response.getheaders(), response.status, response.reason, response.version)
    body = response.read()
    printHeaderTextInfo(headers)
    printBodyTextInfo(body)
    client.closeConnection()
    

#Creamos la ventana inicial
window = Tk();
window.title("HTTP Client")
window.geometry("820x780");

#Creamos el frame donde estara el form para introducir los datos
formFrame = Frame(window, relief = "groove")
formFrame.pack()

urlLabel = Label(formFrame, text = "URL: ").grid(row = 0, column = 0, padx = 5, pady = 5)

sendUrlEntry = Entry(formFrame)
sendUrlEntry.grid(row = 0, column = 1, padx = 5, pady = 5)
sendUrlEntry.config(width = 50)

#Se cambia el height por si se quiere agregar mas de dos metodos
#option es una variable global que guardara la opcion seleccionada
option = StringVar()
methodComboBox = ttk.Combobox(formFrame, textvariable = option, values = ["GET", "HEAD"], state = "readonly")
methodComboBox.current(0)
methodComboBox.grid(row = 0, column = 2, padx = 5, pady = 5)


sendRequestBtn = Button(formFrame, text = "Enviar Solicitud")
sendRequestBtn.config(command = pressSendRequestBtn)
sendRequestBtn.config(activebackground = '#809096')
sendRequestBtn.grid(row = 0, column = 3, padx = 5, pady = 5)


#Creamos el frame donde estara la cabecera de la respuesta del host
headerFrame = Frame(window, relief = "groove")
headerFrame.pack()

headerResponseLabel = Label(headerFrame, text = "Cabeceras de Respuesta: ")
headerResponseLabel.grid(row = 0, column = 0, padx = 5, pady = 5)


headerText = Text(headerFrame, width = 90, height = 15)
headerText.grid(row = 1, column = 0, padx = 5, pady = 5)
#headerText.insert("1.0" ,"texto alternativo")

#Creamos el frame donde estara el cuerpo de la respuesta del host

bodyFrame = Frame(window, relief = "groove")
bodyFrame.pack()

bodyResponseLabel = Label(bodyFrame, text = "Cuerpo/Contenido: ")
bodyResponseLabel.grid(row = 0, column = 0, padx = 5, pady = 5)

bodyText = Text(bodyFrame, width = 90, height = 15)
bodyText.grid(row = 1, column = 0, padx = 5, pady = 5)



# Iniciar la ventana
window.mainloop()

