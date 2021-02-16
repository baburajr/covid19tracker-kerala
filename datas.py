import pandas as pd
import requests

def kl_data():
    r = requests.get('https://keralastats.coronasafe.live/histories.json')
    df = r.json()
    for item in df['histories']:
        data = pd.DataFrame(item['summary'])
    return data.T


def get_districts():
    import requests
    r = requests.get('https://keralastats.coronasafe.live/latest.json')
    data = r.json()
    return data
