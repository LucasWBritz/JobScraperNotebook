from bs4 import BeautifulSoup
import urllib.request

def downloadLink(link):
    return urllib.request.urlopen(link).read().decode("utf-8")

def getAttrFromTag(tag, name):
    return tag.get(name)

def downloadAndParseLink(link):
    return BeautifulSoup(downloadLink(link), 'html.parser')