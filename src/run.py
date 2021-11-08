#coding=utf-8

import requests

url = "https://www.52wubi.com/wbbmcx/tp/我.gif"
#
res = requests.get(url)
#
with open("/Users/feiyue/Documents/WubiDictForMac/gifs/我.gif","wb")as f:
    f.write(res.content)

print("aaa")