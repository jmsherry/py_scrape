#!/usr/bin/python3
import sys
import re
from lxml import html
import requests
from bs4 import BeautifulSoup


def scrape(args):
  if (len(args) != 3):
    print(f'''
      Usage: python3 {args[0]} <url> <tagname>
    ''')
    return
  
  regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  print('args[1]', args[1])
  if (not re.match(regex, args[1])):
    raise('Not a valid URL')

  page = requests.get(args[1])
  soup = BeautifulSoup(page.content, 'html.parser')

  for el in soup.find_all(args[2]):
    print(el)

if (__name__ == '__main__'):
  scrape(sys.argv)