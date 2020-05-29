import http.client
import mimetypes
import json
from datetime import date, datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    return abs((d2 - d1).days)

conn = http.client.HTTPConnection("127.0.0.1", 8000)
payload = ''
headers = {}
conn.request("GET", "/json_view/Employees/", payload, headers)
res = conn.getresponse()
data = res.read()
dd = data.decode("utf-8")
jdata = json.loads(data)
avg = 0
qty = 0
for d in jdata:
    for key, value in d.items():
        if key == "salary":
            avg += value
            qty += 1
file = open('rise.txt', 'w')
avg = int(avg/qty)
file.write('The average salary in ACME company is: '+ str(avg) + '\n \n')
dt = datetime.combine(date.today(), datetime.min.time())
for dz in jdata:
    vetek = days_between(dz['hire_date'], dt)
    if vetek > 365:
        if dz['salary'] < avg:
            file.write(dz['first_name'] + ' ' + dz['last_name'] + ' needs a raise \n')
file.close()