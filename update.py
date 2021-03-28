from requests import get
import json, CloudFlare
ip = get('http://ipgrab.io').text
print('My public IP address is: {}'.format(ip))

cf = CloudFlare.CloudFlare(token="M-vBmz1HZTEQ5YKQTA2z_sLz5w9Deps-UzRIBm4c")
zones = cf.zones.get(params={'per_page':5})
print (zones)
