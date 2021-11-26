
import re
from requests_html import HTMLSession
import ssl

def getInfo(url):
    session = HTMLSession()
    html = session.get(url)
    html_source_code = html.text
    
    numbers = re.findall(r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",html_source_code)
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",html_source_code)

    phoneNmail = dict()

    phoneNmail['Emails'] = emails
    phoneNmail['Phones'] = numbers
    
    if emails:
        print(" ✓ Emails found on this website-\n")
        for mail_id in emails:
            print('     ',mail_id)
    else:
        print(" ✘ No Emails found on this website.")

    print()
    print('{:*^130}'.format(''), '\n')

    if numbers:
        print(" ✓ Phone numbers found on this website- \n")
        for phone_no in numbers:
            print('     ', phone_no)
    else:
        print(" ✘ No Contacts found on this website.")

    return phoneNmail
    
# print(getInfo('https://www.codingninjas.com/'))
