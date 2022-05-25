import xmlrpc.client
import sys


# Informationen
argumentsList = sys.argv
hostAddress = '127.0.0.1'
hostPort = '12345'
URI = "http://" + hostAddress + ":" + hostPort

x = input("x: ")

proxy = xmlrpc.client.ServerProxy(URI)


print('{}'.format(proxy.drawBoard(x)))
print(URI)
