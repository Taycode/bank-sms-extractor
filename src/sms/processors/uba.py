import re


def uba_processor(message: str):
    """Processes UBA SMS"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Txn: Credit|Debit', message)
    transaction_type = transaction_type[0]
    transaction_type = transaction_type[len('Txn: '):]
    transaction_type = transaction_type.lower()

    # Fetch account number
    account_number = re.findall(r'Ac:\w+[.*]+\d+\w', message)
    account_number = account_number[0]
    account_number = account_number[len('Ac:'):]

    # Fetch Description
    description = re.findall(r'Des:.*?(?:(?!\\n).)*', message)
    description = description[0]
    description = description[len('Des:'):]

    # Fetch Amount
    amount = re.findall(r'Amt:NGN.*?(?:(?!\\n).)*', message)
    amount = amount[0]
    amount = amount[len('Amt:NGN '):]

    # Fetch Date
    date = re.findall(r'Date:.*?(?:(?!\\n).)*',message)
    date = date[0]
    date = date[len('Date:'):]

    # Fetch Balance
    balance = re.findall(r'Bal:NGN*?(?:(?!\\n).)*', message)
    balance = balance[0]
    balance = balance[len('Bal:NGN '):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
