#!/usr/bin/python
# -*- coding: UTF-8 -*-
#把某站优异接口的妹子图片爬下来
import requests

def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)

for i in range(10,2250):
    url = 'http://api.isoyu.com/uploads/2017/07/mm_'+str(i)+'.jpg'
    filePath = 'E://'+str(i)+'.jpg'
    dowloadPic(url,filePath)
    print(''+str(i)+' successed')
