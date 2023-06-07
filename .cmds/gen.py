import random

def generate_random_cc(bin_number='random'):
    # Generate random BIN if not provided
    if bin_number == 'random':
        bin_number = ''.join(random.choice('0123456789') for _ in range(6))

    # Generate random card number (excluding last digit)
    card_number = bin_number + ''.join(random.choice('0123456789') for _ in range(9))

    # Generate random expiration date (month and year)
    expiration_month = random.randint(1, 12)
    expiration_year = random.randint(2023, 2030)

    # Generate random CVV code (3 digits)
    cvv = ''.join(random.choice('0123456789') for _ in range(3))

    # Format the generated data
    formatted_card_number = '-'.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
    formatted_expiration = f'{expiration_month}/{expiration_year}'

    return formatted_card_number, formatted_expiration, cvv

# Example usage
amount = int(input('Enter the amount of credit card numbers to generate: '))
bin_number = input('Enter the BIN number (or leave blank for random): ')

for _ in range(amount):
    card_number, expiration, cvv = generate_random_cc(bin_number)
    print(f'Card: {card_number} | Expiration: {expiration} | CVV: {cvv}')
