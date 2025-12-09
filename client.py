import http.client
import urllib.parse

class HTTPClient:
    def __init__(self):
        self.conn = None

    def connectToHost(self, url, method):
        parsed = urllib.parse.urlparse(url)
        
        if not parsed.scheme:
            url = "https://" + url
            parsed = urllib.parse.urlparse(url)
        
        host = parsed.hostname
        port = parsed.port
        path = parsed.path if parsed.path else "/"
        if parsed.query:
            path += "?" + parsed.query
        
        if parsed.scheme == "https":
            if port:
                self.conn = http.client.HTTPSConnection(host, port)
            else:
                self.conn = http.client.HTTPSConnection(host)
        else:
            if port:
                self.conn = http.client.HTTPConnection(host, port)
            else:
                self.conn = http.client.HTTPConnection(host)
        
        self.conn.request(method, path, headers={"Host": host})
        return self.conn

    def sendRequest(self, url, method):
        self.connectToHost(url, method)
        response = self.conn.getresponse() 
        return response

    def closeConnection(self):
        if self.conn:
            self.conn.close()







        

    



