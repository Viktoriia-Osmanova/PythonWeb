import aiohttp
import asyncio
import argparse
from datetime import datetime, timedelta

async def fetch_exchange_rate(session, date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    async with session.get(url) as response:
        data = await response.json()
        return data

async def get_exchange_rates(days):
    async with aiohttp.ClientSession() as session:
        tasks = []
        current_date = datetime.now()
        
        for _ in range(days):
            date_str = current_date.strftime('%d.%m.%Y')
            task = fetch_exchange_rate(session, date_str)
            tasks.append(task)
            current_date -= timedelta(days=1)

        results = await asyncio.gather(*tasks)
        return results

def parse_args():
    parser = argparse.ArgumentParser(description='Get exchange rates for EUR and USD from PrivatBank API.')
    parser.add_argument('days', type=int, help='Number of days to retrieve exchange rates (up to 10 days)')
    return parser.parse_args()

def main():
    args = parse_args()
    
    if not 1 <= args.days <= 10:
        print("Error: Number of days should be between 1 and 10.")
        return
    
    loop = asyncio.get_event_loop()
    exchange_rates = loop.run_until_complete(get_exchange_rates(args.days))
    
    result = []
    for i, rate_data in enumerate(exchange_rates):
        date_str = (datetime.now() - timedelta(days=i)).strftime('%d.%m.%Y')
        rates = {
            'EUR': {
                'sale': rate_data['exchangeRate'][0]['saleRateNB'],
                'purchase': rate_data['exchangeRate'][0]['purchaseRateNB']
            },
            'USD': {
                'sale': rate_data['exchangeRate'][1]['saleRateNB'],
                'purchase': rate_data['exchangeRate'][1]['purchaseRateNB']
            }
        }
        result.append({date_str: rates})

    print(result)

if __name__ == '__main__':
    main()
