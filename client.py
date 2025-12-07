import http.client


def connectToHost(host):
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/", headers = {"Host": host})
    return conn.getresponse()

def sendHttpRequest(host):
    print(f"HTTP request Sent to {host}")
    response = connectToHost(host)
    print(response.status, response.reason)
