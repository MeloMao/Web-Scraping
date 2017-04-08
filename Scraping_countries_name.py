#coding=utf-8
import urllib2
import itertools
import re

def download(url):
   # print 'Downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Donwnload error:',e.reason
        html=None
    print re.findall('<td class="w2p_fw">(.*?)</td>',html)[4]
    return html

max_errors=5
num_errors=0
for page in itertools.count(1):
    url='http://example.webscraping.com/view/-%d' % page
    html=download(url)
    #print html
    if html is None:
        num_errors += 1
        if num_errors==max_errors:
            break
    else:
        num_errors=0
