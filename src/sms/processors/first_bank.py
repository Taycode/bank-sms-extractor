import re


def first_bank_processor(message: str):
    """Processes first bank sms"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Debit|Credit', message)  # returns array of matches
    transaction_type = transaction_type[0]  # Fetches first result in array
    transaction_type = transaction_type.lower()  # turns to lowercase

    # Fetch Description using regex
    description = re.findall(r'Desc: \w+.*', message)  # returns array
    description = description[0]  # returns 'Desc: xxxxxx'
    description = description[len('Desc: '):]  # Removes 'Desc: '

    return {
        'description': description,
        'transaction_type': transaction_type,
    }
