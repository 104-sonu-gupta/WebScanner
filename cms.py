from urllib.request import urlopen



def get_cms(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'
    print(" ✓ Detecting CMS used..... ")
    try:
        html=urlopen(path+"robots.txt")
        c=html.read().decode('utf-8')

        if '/wp-admin/' in c:
            print("WordPress")
        elif '/_api/*' in c:
            print("Wix")
        elif 'Joomla' in c:
            print("Joomla")
        else:
            print("\n ✘ Cannot Identify CMS used ")  
        return(html.read().decode('utf-8'))
    except:
        print("\n ✘ Cannot Identify CMS used ")
  
 
