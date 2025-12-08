import http.client

class HTTPClient:
    def __init__(self):
        self.conn = None

    def connectToHost(self, host, method):
        self.conn = http.client.HTTPSConnection(host)
        self.conn.request(method, "/", headers = {"Host": host})
        return self.conn

    def sendRequest(self, host, method):
        self.connectToHost(host, method)
        response = self.conn.getresponse() 
        return response

    def closeConnection(self):
        if self.conn:
            self.conn.close()







        

    



