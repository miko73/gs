#IMPORTS
import requests
import time
from bs4 import BeautifulSoup

import re
#CONSTRAINTS
EMAIL = 'michal.kocandrle@gmail.com'
PASSW = '7Kokosak3'
LOGIN_URL = "https://www.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&amp;refid=8"
FACEBOOK_URL = "http://www.facebook.com"

#VARS
s = None

#MAIN CLASS
class facebook():
    def __init__(self):
        self.s = requests.session()
        self.login()
        self.find_accounts_by_name()

    def login(self):
        #GET DEFAULT VALUES FROM PAGE
        r = self.s.get(FACEBOOK_URL, verify=False)
        print (r.text)
        soup = BeautifulSoup(r.text)
        #GET DEFAULT VALUES
        tmp = soup.find(attrs={"name": "lsd"})
        lsd = tmp["value"]

        data = {
            'lsd': lsd
        }
        data['email'] = EMAIL
        data['pass'] = PASSW
        data['login'] = 'Log In'

        r = self.s.post(LOGIN_URL , data=data, verify=False)
        print (r.text)

# fb = facebook()

def facebook_login(mail, pwd):
    session = requests.Session()
    r = session.get('https://www.facebook.com/', allow_redirects=False)
    soup = BeautifulSoup(r.text)
    action_url = soup.find('form', id='login_form')['action']
    inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
    post_data = {input.get('name'): input.get('value')  for input in inputs}
    post_data['email'] = mail
    post_data['pass'] = pwd.upper()
    scripts = soup.findAll('script')
    scripts_string = '/n/'.join([script.text for script in scripts])
    datr_search = re.search('\["_js_datr","([^"]*)"', scripts_string, re.DOTALL)
    if datr_search:
        datr = datr_search.group(1)
        cookies = {'_js_datr' : datr}
    else:
        return False
    return session.post(action_url, data=post_data, cookies=cookies, allow_redirects=False)

if facebook_login(EMAIL, PASSW):
    print("Successfull login")
else:
    print ("Not logged in")
