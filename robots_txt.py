from urllib.request import urlopen

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url+'/'
    try:
        html = urlopen(path + "robots.txt")
        print(' ✓ robots.txt of the following site has the following data: ')
        return str(html.read().decode('utf-8'))
    except:
        print(" ✘ Cannot get robots.txt of the given website ")
