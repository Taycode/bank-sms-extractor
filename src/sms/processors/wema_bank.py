import re


def wema_bank_processor(message: str):
    """Processes Wema SMS"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Credit|Debit', message)
    transaction_type = transaction_type[0]
    transaction_type = transaction_type.lower()

    # Fetch account number
    account_number = re.findall(r'Acct No:\w+[.*]+\d+\w', message)
    account_number = account_number[0]
    account_number = account_number[len('Acct No:'):]

    # Fetch Description
    description = re.findall(r'Desc.:*?(?:(?!\r).)*', message)
    description = description[0]
    description = description[len('Desc.: '):]

    # Fetch Amount
    amount = re.findall(r'.*NGN[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('NGN'):]

    # Fetch Date
    date = re.findall(r'.*\d{2}-\d{2}-\d{4} \d+:\d+', message)
    date = date[0]
    
    # Fetch Balance
    balance = re.findall(r'Bal: [\d+,]+.\d+', message)
    balance = balance[0]
    balance = balance[len('Bal: '):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
