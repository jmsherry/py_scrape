#!/usr/bin/python3
import sys
import re
import requests
from bs4 import BeautifulSoup

def scrape(args):
  if (len(args) != 3):
    raise(f'''
      Usage: python3 {args[0]} <url> <tagname>
    ''')
  
  regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  # print('URL', args[1])
  if (not re.match(regex, args[1])):
    raise(f'{args[1]} is not a valid URL')

  page = requests.get(args[1])
  soup = BeautifulSoup(page.content, 'html.parser')

  print('\n')
  for el in soup.find_all(args[2]):
    print(el, '\n')

if (__name__ == '__main__'):
  scrape(sys.argv)