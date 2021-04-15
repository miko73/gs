import requests
import pyCookieCheat


# jar = requests.cookies.RequestsCookieJar([
# {
#     "domain": ".stackoverflow.com",
#     "expirationDate": "1427212131.77312",
#     "hostOnly": "false",
#     "httpOnly": "true",
#     "name": "usr",
#     "path": "/",
#     "secure": "false",
#     "session": "false",
#     "storeId": "0",
#     "value": "SOMEVALUE",
#     "id": "5"
# }]
# requests.get(url, headers=headers, cookies=jar)


url = 'https://www.itnetwork.cz/'

s = requests.Session()
cookies = pyCookieCheat.chrome_cookies(url)
s.get(url, cookies = cookies)
print (f'{s}')