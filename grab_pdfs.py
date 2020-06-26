# Created by happygirlzt
from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.parse import urljoin
import urllib.error, urllib.request
import os
import os.path
import sys
import time

url=input("[+] Enter the download path in full: ")
suffix=input("[+] Enter the file type you want to save (e.g., pdf): ")
saved_path=input("[+] Enter the relative path you want to save the files: ")

html=urllib.request.urlopen(url)
soup=bs(html.read(),features="lxml")
i=0

for tag in soup.find_all('a', href=True):
    #print(tag)
    tag['href']=urljoin(url, tag['href'])
    #print(tag['href'])

    if os.path.splitext(os.path.basename(tag['href']))[1] == '.'+suffix:
        try:
            i+=1
            current=urllib.request.urlopen(tag['href'])
            start=time.time()
            print("\n[*] Downloading: {}".format(os.path.basename(tag['href'])))
            if os.path.exists(saved_path+os.path.basename(tag['href'])):
                print('Already downloaded')
                continue
            
            f=open(saved_path + os.path.basename(tag['href']), 'wb')
            f.write(current.read())
            f.close()
            end = time.time()
            print("It takes {} s".format(end - start))
        except 'urllib.error.HTTPError':
            print('hmmm, error')
            continue

print("\n[*] Downloaded {} files".format(i+1))