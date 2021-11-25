import os

def tracert(x):
    print(' ✓ Traceroute-')
    my_command = f'tracert {x}'
    os.system(my_command)

#x=str(input("Enter website:"))
#tracert(x)
