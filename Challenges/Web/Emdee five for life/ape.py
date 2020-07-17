import re, hashlib, requests
from bs4 import BeautifulSoup

s = requests.Session()
URL = 'http://docker.hackthebox.eu:30315/'
page = s.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
q = re.findall(r"<h3.*\"center\">(.*)</h3>", soup.decode())
dt = {'hash': hashlib.md5(q[0].encode()).hexdigest()}
x = s.post(URL, data = dt)
print(x.text)


