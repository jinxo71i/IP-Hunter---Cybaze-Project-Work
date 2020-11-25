import socket
import whois

'''x = input ("\nPlease enter a domain name that you wish to translate: ")
print ("\n\nThe IP Address of the Domain Name is: "+str(socket.gethostbyname_ex(x)))'''


w = whois.whois("2.32.34.44")
print(w)