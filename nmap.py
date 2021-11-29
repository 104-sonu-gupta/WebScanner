import nmap3


def get_nmap(domain_name):
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(domain_name)
    ip = list(results.keys())[0]
    data = results[ip]
    print(" ✓ Port Scanning using network mapper\n")
    print("    #\tPort Number\tService Name")
    i = 1
    nmap_result = ''
    for port in data['ports']:
        print("   ", i, "\t", port['portid'], "\t\t", port['service']['name'])
        nmap_result += f"""{i}\t {port['portid']}\t \t{port['service']['name']}\n"""
        i += 1

    return nmap_result

    # results = nmap.scan_top_ports(domain_name, 20)
