import http.client
import urllib.parse

conn = None

def connectToHost(host, method):
    global conn
    conn = http.client.HTTPSConnection(host)
    conn.request(method, "/", headers = {"Host": host})
    return conn

def sendRequest(host, method):
    global conn
    print(f"HTTP request Sent to {host}")
    if(method == "GET"):
        conn = connectToHost(host, method)
    elif(method == "HEAD"):
        conn = connectToHost(host, method)
    response = conn.getresponse()
    print(response.status, response.reason)
    print(f"Content-Type: {response.getheader('Content-Type')}")
    print(f"Server: {response.getheader('Server')}")
    print(f"Date: {response.getheader('Date')}")
    print(f"Content-Length: {response.getheader('Content-Length')}") 
    print(f"Cache-Control: {response.getheader('Cache-Control')}")
    return response
    

    


def closeConnection():
    conn.close()

