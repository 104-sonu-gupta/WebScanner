from tld import get_fld

def get_domain_name(url):
    domain_name = get_fld(url)
    print(" ✓ Domain Name is : " + domain_name)
    return domain_name

# get_domain_name("https://www.google.com")