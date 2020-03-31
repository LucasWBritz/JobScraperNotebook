from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib.parse

def downloadLink(link):
    req = urllib.request.Request(link, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    )
    return urllib.request.urlopen(req).read().decode("utf-8")

def getAttrFromTag(tag, name):
    return tag.get(name)

def downloadAndParseLink(link):
    return BeautifulSoup(downloadLink(link), 'html.parser')

def encodeString(string):
    return urllib.parse.quote(string)