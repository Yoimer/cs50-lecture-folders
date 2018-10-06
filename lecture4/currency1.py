import os, requests

def main():
    # Figure out our API_KEY, stored as environment variable.
    apikey = os.getenv('API_KEY')

    # Format a GET request to Fixer API, plugging in parameters.
    res = requests.get(f'http://data.fixer.io/api/latest?access_key={apikey}&base=EUR&symbols=USD')

    # Check that everything worked.
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert the response to JSON and print out the relevant parts.
    data = res.json()
    rate = data['rates']['USD']
    print(f'1 EUR is equal to {rate} USD')

if __name__ == '__main__':
    main()
