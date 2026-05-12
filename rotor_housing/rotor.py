import requests

def ask():
    return requests.get('http://rotor').json()