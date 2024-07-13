import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_cmc_data():
    url = "https://coinmarketcap.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'cmc-table'})
    rows = table.find_all('tr')
    data = []
    total_market_cap = 0

    for row in rows[1:]:
        cols = row.find_all('td')
        mc = cols[3].text.strip().replace('$', '').replace(',', '')
        mc = float(mc)
        total_market_cap += mc

    for row in rows[1:]:
        cols = row.find_all('td')
        name = cols[2].text.strip()
        mc = cols[3].text.strip().replace('$', '').replace(',', '')
        try:
            mc = float(mc)
        except ValueError:
            mc = 0
        mp = round((mc / total_market_cap) * 100, 2) if total_market_cap != 0 else 0

        data.append({'Name': name, 'Market Cap': mc, 'Market Percentage': mp})

    return data


def write_cmc_top(data):
    now = datetime.now().strftime("%H.%M_%d.%m.%Y")
    filename = f"{now}.csv"

    df = pd.DataFrame(data)
    df.to_csv(filename, sep=' ', index=False)


if __name__ == "__main__":
    data = get_cmc_data()
    write_cmc_top(data)