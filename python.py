from urllib.request import urlopen
from urllib.error import *
url = "https://atg.world/"
try:
    urlopen(url)
except URLError as e:
    print("Page not found : ",e)
else:
    print("Hello World!")

