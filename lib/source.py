import sys, core, re
from lib.logger import logger
from bs4 import BeautifulSoup

def get_reverse_from_resolvethem(name):
    url = 'http://www.resolvethem.com/'
    html = core.get_html_from_url(url, name)
    if html:
        parser = BeautifulSoup(html)
        data = parser.find('div','inner')
        ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", data.get_text())
        if ip:
            if  re.match("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", ip.group(0)):
                return ip.group(0)
            else:
                return False
        else:
            return False







#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.
#Copyright RLC. IV.