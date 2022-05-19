import re


def access_bank_processor(message :str):
    """Processes Access Bank SMS"""

    # Fetch transaction type
    transaction_type = re.findall(r'Credit|Debit', message)
    transaction_type = transaction_type[0]

    # Fetch account number
    account_number = re.findall(r'Acc:\w+[*]+\d+', message)
    account_number = account_number[0]
    account_number = account_number[len('Acc:'):]

    # Fetch Description
    description = re.findall(r'Desc:\w+.*?(?:(?!\sTime).)*', message)
    description = description[0]
    description = description[len('Desc:'):]

    # Fetch Amount
    amount = re.findall(r'Amt:NGN[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('Amt:NGN'):]

    # Fetch Date
    date = re.findall(r'Time:.*?(?:(?!\s).)*', message)
    date = date[0]
    date = date[len('Time:'):]

    # Fetch Balance
    balance = re.findall(r'Bal:NGN.*?(?:(?!\s).)*', message)
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
