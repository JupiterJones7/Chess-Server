import xmlrpc.client
import sys



argumentsList = sys.argv
hostAddress = '127.0.0.1'
hostPort = '1111'
URI = "http://" + hostAddress + ":" + hostPort

proxy = xmlrpc.client.ServerProxy(URI)

x = 1
print('{}'.format(proxy.ausführen(x)))
print(URI)
