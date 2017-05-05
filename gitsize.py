#!/usr/bin/python3

import requests
import sys

url = sys.argv[1]
sec = url[4]
if sec=="s":
    url = "https://api.github.com/repos/"+url[19:]
else:
    url = "https://api.github.com/repos/"+url[18:]
print(url)
page = requests.get(url)
page.raise_for_status()
json = page.json()
print(json['full_name'])
size = json['size']
size = size/1000
print(size,end='')
print("Mb")

