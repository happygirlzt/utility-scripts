#
# Created on Wed May 19 2021
#
# Copyright (c) 2021 happygirlzt
#

from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.parse import urljoin
import urllib.error, urllib.request
import os
import os.path
import sys
import time

def main():
    url = input("[+] Enter the download path in full: ")
    # suffix = input("[+] Enter the file type you want to save (e.g., pdf): ")

    suffix = 'pdf'
    html = urllib.request.urlopen(url)
    # soup = bs(html.read(), features="lxml")
    soup = bs(html.read(),  "html.parser")

    i = 0

    for tag in soup.find_all('a', href = True):
        #print(tag)
        tag['href']=urljoin(url, tag['href'])
        #print(tag['href'])

        if os.path.splitext(os.path.basename(tag['href']))[1] == '.'+suffix:
            try:
                i += 1
                current = urllib.request.urlopen(tag['href'])
                start = time.time()
                print("\n[*] Downloading: {}".format(os.path.basename(tag['href'])))
                if os.path.exists(os.path.basename(tag['href'])):
                    print('Already downloaded')
                    continue
                
                f = open(os.path.basename(tag['href']), 'wb')
                f.write(current.read())
                f.close()
                end = time.time()
                print("It takes {} s".format(end - start))
            except KeyboardInterrupt:
                sys.exit(0)
            # except 'urllib.error.HTTPError':
            except:
                print('hmmm, error')
                continue

    print("\n[*] Downloaded {} files".format(i+1))
    
if __name__ == '__main__':
    main()