import socket

def get_ip_address(url):
    results = socket.gethostbyname(url)
    print(" ✓ IP Address is : " + results)
    return results
