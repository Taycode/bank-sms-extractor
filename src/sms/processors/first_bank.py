import re


def first_bank_processor(message: str):
    """Processes first bank sms"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Debit|Credit', message)  # returns array of matches
    transaction_type = transaction_type[0]  # Fetches first result in array

    # Fetch Account Number
    account_number = re.findall(rf'{transaction_type}: \w+', message)
    account_number = account_number[0]
    account_number = account_number[len(f'{transaction_type}: '):]

    transaction_type = transaction_type.lower()  # turns to lowercase

    # Fetch Description using regex
    description = re.findall(r'Desc: \w+.*', message)  # returns array
    description = description[0]  # returns 'Desc: XXX...'
    description = description[len('Desc: '):]  # Removes 'Desc: '

    # Fetch Amount
    amount = re.findall(r'Amt: NGN(?:(?!\s).)*', message)
    amount = amount[0]
    amount = amount[len('Amt: NGN'):]

    # Fetch Date
    date = re.findall(r'Date: (?:(?!\sDesc).)*', message)
    date = date[0]
    date = date[len('Date: '):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'date': date
    }
