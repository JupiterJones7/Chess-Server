import xmlrpc.client
import sys



argumentsList = sys.argv
hostAddress = '127.0.0.1'
hostPort = '12345'
URI = "http://" + hostAddress + ":" + hostPort
print(URI)

proxy = xmlrpc.client.ServerProxy(URI)
input1 = input("Where do you wanna place your figure: ")
print('{}'.format(proxy.main(input1)))
