import re 


def keystone_bank_processor(message: str):
    """Processes Keystone Bank sms"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Debit|Credit', message)
    transaction_type = transaction_type[0]
    transaction_type = transaction_type.lower()

    # Fetch account number
    account_number = re.findall(r'Acct:\w+[*]+\d+', message)
    account_number = account_number[0]
    account_number = account_number[len('Acc:'):]

    # Fetch Description
    description = re.findall(r'Desc:.*?(?:(?!\\n).)*', message)
    description = description[0]
    description = description[len('Desc:'):]

    # Fetch Amount
    amount = re.findall(r'Amt:N.*?(?:(?!\\n).)*', message)
    amount = amount[0]
    amount = amount[len('Amt:N'):]

    # Fetch Date
    date = re.findall(r'Date:.*?(?:(?!\\n).)*', message)
    date = date[0]
    date = date[len('Date:'):]

    # Fetch Balance
    balance = re.findall(r'Bal:NGN*?(?:(?!\\n).)*', message)
    balance = balance[0]
    balance = balance[len('Bal:NGN'):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
