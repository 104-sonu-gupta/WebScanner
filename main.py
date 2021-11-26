from general import *
from domain_name import *
from robots_txt import *
from nmap import get_nmap
from ip_addr import *
from extractPII import *
from webcrawler import *
from traceroute import *
from nslookup import *
from cms import *
import os, json
from art import *

root_dir = 'Stored_Websites'
create_dir(root_dir)
os.system('cls')


def liner():
    print()
    print('{:*^130}'.format(''), '\n')


def gather_info(name, url):

    liner()
    domain_name = get_domain_name(url)
    liner()
    ip_addr = get_ip_address(domain_name)
    liner()

    nmap = get_nmap(domain_name)
    liner()

    robots_txt = get_robots_txt(url)
    if robots_txt:
        print(robots_txt)
    liner()

    get_cms(url)
    liner()

    tracert(domain_name)
    liner()

    links = ('\n\n').join(getLinks(url))
    liner()

    phoneNemail = getInfo(url)
    phoneNemail = json.dumps(phoneNemail, indent=4, sort_keys=True)
    liner()

    nsInfo = getDNSInfo(domain_name)
    liner()

    create_report(name, url, domain_name, nmap, robots_txt,
                  ip_addr, links, phoneNemail, nsInfo)


def create_report(name, full_url, domain_name, nmap, robots_txt, ip_addr, links, phoneNemail, nsInfo):

    project_dir = root_dir + '/' + name
    create_dir(project_dir)

    general_details = f""" 
    
    domain name : {str(domain_name)}
    
    Full URL    : {str(full_url)}
    
    IP Address  : {str(ip_addr)}
    """

    write_file(project_dir + '/general_details.txt', general_details)
    write_file(project_dir + '/nmap.txt', str(nmap))
    write_file(project_dir + '/robots.txt', str(robots_txt))
    write_file(project_dir + '/links.txt', str(links))
    write_file(project_dir + '/Phone_Emails.txt', str(phoneNemail))
    write_file(project_dir + '/server_info.txt', str(nsInfo))


tprint("Website  Scanner")


website_name = str(input("Enter folder's name to save website's data name : "))
print("\n ⚠ Note: Enter site in the following format only : http://www.<website>")
website_url = str(input('\nEnter address of website to scan : '))

gather_info(website_name, website_url)

# gather_info("Apache", "http://www.apache.org")

# gather_info("NGINX", "http://www.nginx.org")

# gather_info("Google", "https://www.google.com")

# gather_info("CodingNinja", "https://www.codingninjas.com")

# gather_info("Facebook", "https://www.facebook.com")

# gather_info("Amazon", "https://www.amazon.in/")
