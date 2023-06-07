import requests

def is_valid_credit_card(card_info):
    # Split the card information
    card_data = card_info.split("|")
    if len(card_data) != 4:
        return False

    number = card_data[0]
    month = card_data[1]
    year = card_data[2]
    cvv = card_data[3]

    # Perform basic length and format checks
    if len(number) != 16 or not number.isdigit():
        return False
    if len(month) != 2 or not month.isdigit():
        return False
    if len(year) != 4 or not year.isdigit():
        return False
    if len(cvv) != 3 or not cvv.isdigit():
        return False

    # Validate credit card using binlist.net API
    bin_number = number[:6]
    api_url = f"https://lookup.binlist.net/{bin_number}"
    headers = {"Accept-Version": "3"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        card_data = response.json()
        if "bank" in card_data and "name" in card_data["bank"]:
            return True
        else:
            return False
    else:
        return False

# Example usage
credit_card_info = input("Enter the credit card information (Format: cardno.|month|year|cvv): ")
credit_cards = credit_card_info.split("\n")

for card in credit_cards:
    if is_valid_credit_card(card):
        print(f"The credit card '{card}' is valid.")
    else:
        print(f"The credit card '{card}' is not valid.")
