import re


def polaris_bank_processor(message: str):
    """Processes Polaris Bank SMS"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Credit|Debit', message)
    transaction_type = transaction_type[0]
    transaction_type = transaction_type.lower()

    # Fetch account number
    account_number = re.findall(r'Acct:.*?(?:(?!\\n).)*', message)
    account_number = account_number[0]
    account_number = account_number[len('Acct:'):]

    # Fetch Description
    description = re.findall(r'Ref:*?(?:(?!\\n).)*', message)
    description = description[0]
    description = description[len('Ref: '):]

    # Fetch Amount
    amount = re.findall(r'Amt:N[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('Amt:N'):]

    # Fetch Date
    date = re.findall(r'.*\d{2}-\d{2}-\d{6}:\d+', message)
    date = date[0]
    
    # Fetch Balance
    balance = re.findall(r'Bal:N.*?(?:(?!\\n).)*', message)
    balance = balance[0]
    balance = balance[len('Bal:N'):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
