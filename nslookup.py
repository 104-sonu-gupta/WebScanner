import subprocess
import sys

def getDNSInfo(url):
    print("NSLOOKUP using SOA -")
    type
    command = "nslookup -type=" + "SOA " + url
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if(error):
        print(error)
    print()
    
    print(output.decode("utf=8"))
    return(output.decode("utf=8"))

# getDNSInfo("analyticsindiamag.com")