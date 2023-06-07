import requests

def bin_checker(bin_number):
    # BIN number API endpoint
    api_url = f'https://lookup.binlist.net/{bin_number}'

    try:
        # Send GET request to the BIN number API
        response = requests.get(api_url)

        # Check if request was successful
        if response.status_code == 200:
            bin_info = response.json()

            # Extract relevant information from the response
            bank_name = bin_info.get('bank', {}).get('name')
            country = bin_info.get('country', {}).get('name')
            brand = bin_info.get('brand')
            card_type = bin_info.get('type')

            # Print the BIN information
            print(f'Bank: {bank_name}')
            print(f'Country: {country}')
            print(f'Brand: {brand}')
            print(f'Card Type: {card_type}')

        else:
            print('Error occurred while retrieving BIN information. Please try again.')

    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')

# Example usage
bin_number = input('Enter the BIN number to check: ')
bin_checker(bin_number)
