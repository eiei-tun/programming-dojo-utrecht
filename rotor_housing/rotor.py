import requests

def ask(q):
    return requests.get('http://rotor', params={
        q: q
    }).json()