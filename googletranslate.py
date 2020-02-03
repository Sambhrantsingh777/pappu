# -*- coding: UTF-8 -*-
import os
import requests
import random
import time
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


device_data = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; en-us; A5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750 Mobile Safari/537.36", }


def random_generate(size):
    alpha_numeric_elements = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    random_string = ''.join(random.choice(alpha_numeric_elements) for i in range(size))
    return random_string

##################################################
#
#   name holds the value to be translated
#
##################################################
def google_trans(name):
    url = 'https://www.google.com/async/translate'
    headers = {
        'Origin': 'https://www.google.com',
        'User-Agent': device_data.get('User-Agent'),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Referer': 'https://www.google.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',

    }

    data = {
        'async': 'translate,sl:auto,tl:hi,st:' + name + ',id:"' + str(int(time.time() * 1000)) + '",qc:true,ac:true,'
                                                                                                 '_id:tw-async'
                                                                                                 '-translate,_pms:s,'
                                                                                                 '_fmt:pc'}

    params = {
        'vet': random_generate(51),
        'ei': random_generate(22),
        'rlz': random_generate(19),
        'yv': str(random.randint(1, 9)),
    }

    return requests.post(url, headers=headers, params=params, data=data, timeout=30, verify=False)


def start(name):
    result = google_trans(name).text
    # print '#######################################################################'
    # print '#######################################################################'
    soup = BeautifulSoup(result, 'html.parser')
    return soup.find(id="tw-answ-target-text").get_text()
