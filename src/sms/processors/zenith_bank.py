import re


def zenith_bank_processor(message: str):
    """Processes Zenith Bank SMS"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'(CR|DR) Amt', message)
    transaction_type = transaction_type[0]
    transaction_type = 'credit' if transaction_type == 'CR' else 'debit'

    # Fetch account number
    account_number = re.findall(r'Acct:\w+[.*]+\d+\w', message)
    account_number = account_number[0]
    account_number = account_number[len('Acct:'):]

    # Fetch Description
    description = re.findall(r'(?<=\n)(.*?)(?=\n)', message)[1]

    # Fetch Amount
    amount = re.findall(r'Amt:[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('Amt:'):]

    # Fetch Date
    date = re.findall(r'DT:\d{2}/\d{2}/\d{4}:\d+:\d+', message)
    date = date[0]
    date = date[len('DT:'):]

    # Fetch Balance
    balance = re.findall(r'Bal:[\d+,]+.\d+', message)
    balance = balance[0]
    balance = balance[len('Bal:'):]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
