import os, requests

def main():
    # Prompt the user for a currency to convert to.
    target = input('Target Currency: ')

    # Submit a GET request to Fixer, parameterizing our request differently.
    res = requests.get('http://data.fixer.io/api/latest',
                       params={'access_key': os.getenv('API_KEY'),
                               'base': 'EUR',
                               'symbols': target})
    # Check that everything worked.
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert the response to JSON and print out the relevant parts.
    data = res.json()
    if data['success'] == False:
        raise Exception('ERROR: Currency does not exist.')

    rate = data['rates'][target]
    print(f'1 EUR is equal to {rate} {target}')

if __name__ == '__main__':
    main()
