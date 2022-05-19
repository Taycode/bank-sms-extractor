import re


def gtbank_processor(message: str):
    """Processes GtBank sms"""

    # Fetch transaction type
    transaction_type = re.findall(r'\bCR|DR\b', message)
    transaction_type = transaction_type[0]
    transaction_type = 'credit' if transaction_type == 'CR' else 'debit'

    # Fetch account number
    account_number = re.findall(r'Acct: \d+', message)
    account_number = account_number[0]
    account_number = account_number[len('Acc: '):]

    # Fetch Description
    description = re.findall(r'Desc:.*?(?:(?!\\n).)*', message)
    description = description[0]
    description = description[len('Desc:'):]

    # Fetch Amount
    amount = re.findall(r'Amt: NGN[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('Amt: NGN'):]

    # Fetch Date
    date = re.findall(r'Date:.*', message)
    date = date[0]
    date = date[len('Date: '):]

    # Fetch Balance
    balance = re.findall(r'Bal: NGN.*?(?:(?!\\n).)*', message)
    balance = balance[0]
    balance = balance[len('Bal: NGN'):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
