#coding=utf-8

import requests
# 参考: https://www.cnblogs.com/xe2011/p/11583645.html
# 参考: https://www.cnblogs.com/xe2011/p/4315879.html

url = "https://www.52wubi.com/wbbmcx/tp/我.gif"
#
res = requests.get(url)
#
with open("/Users/feiyue/Documents/WubiDictForMac/gifs/我.gif","wb")as f:
    f.write(res.content)

print("aaa")